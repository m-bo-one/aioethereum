import logging
import asyncio
from urllib.parse import urlparse

import aiohttp
import async_timeout

try:
    import ujson as json  # noqa
except ImportError:
    import json

from .errors import BadResponseError, BadStatusError, BadJsonError
from .management import RpcMixin


logger = logging.getLogger('asyncio_client')


_reconnect_times = 3


class AsyncIOIPCClient(RpcMixin):

    def __init__(self, reader, writer, unix_path, timeout=60, *, loop=None):
        self._reader = reader
        self._writer = writer
        self._timeout = timeout
        self._unix_path = unix_path
        self._id = 1
        self._loop = loop or asyncio.get_event_loop()
        self._lock = asyncio.Semaphore(1, loop=self._loop)

    @asyncio.coroutine
    def _call(self, method, params=None, _id=None):
        params = params or []
        data = {
            'jsonrpc': '2.0',
            'method': method,
            'params': params,
            'id': _id or self._id,
        }
        with (yield from self._lock):
            self._writer.write(json.dumps(data).encode('utf-8'))
            b = yield from self._reader.readline()
            if not b:
                tried = 0
                while True:
                    try:
                        new_client = create_ethereum_client(self._unix_path,
                                                            self._timeout)
                    except Exception:
                        tried += 1
                        if tried >= _reconnect_times:
                            self._log.error('_receive: no data, '
                                            'connection refused.')
                            raise ConnectionError('Didn\'t receive any data, '
                                                  'connection refused.')
                self._id = new_client._id
                self._reader = new_client._reader
                self._writer = new_client._writer
                self._lock = new_client._lock
                return self._call(method, params, _id)

        try:
            response = json.loads(b.decode('utf-8'))
        except ValueError:
            raise BadJsonError('Invalid received json from node.')

        if not _id:
            self._id += 1
        try:
            return response['result']
        except KeyError:
            raise BadResponseError(response['error']['message'],
                                   response['error']['code'])


class AsyncIOHTTPClient(RpcMixin):

    def __init__(self, host='127.0.0.1', port=8545, tls=False,
                 timeout=60, *, loop=None):
        self.host = host
        self.port = port
        self.tls = tls
        self._timeout = timeout
        self._id = 1
        self._loop = loop or asyncio.get_event_loop()

    @asyncio.coroutine
    def _call(self, method, params=None, _id=None):
        params = params or []
        data = {
            'jsonrpc': '2.0',
            'method': method,
            'params': params,
            'id': _id or self._id,
        }
        scheme = 'http'
        if self.tls:
            scheme += 's'
        url = '{}://{}:{}'.format(scheme, self.host, self.port)

        try:
            with aiohttp.ClientSession(loop=self._loop) as session:
                with async_timeout.timeout(self._timeout,
                                           loop=self._loop):
                    r = yield from session.post(
                        url=url,
                        data=json.dumps(data),
                        headers={'Content-Type': 'application/json'}
                    )
        except aiohttp.ClientConnectorError as e:
            raise ConnectionError(e)

        if r.status != 200:
            raise BadStatusError(r.status)

        try:
            response = yield from r.json(loads=json.loads)
        except ValueError:
            raise BadJsonError('Invalid received json from node.')

        if not _id:
            self._id += 1
        try:
            return response['result']
        except KeyError:
            raise BadResponseError(response['error']['message'],
                                   response['error']['code'])


@asyncio.coroutine
def create_ethereum_client(uri, timeout=60, *, loop=None):
    presult = urlparse(uri)
    if presult.scheme in ('ipc', 'unix'):
        reader, writer = yield from asyncio.open_unix_connection(presult.path)
        return AsyncIOIPCClient(reader, writer, uri, timeout, loop=loop)
    elif presult.scheme in ('http', 'https'):
        tls = False
        if presult.scheme[-1] == 's':
            tls = True
        netloc = presult.netloc.split(':')
        if len(netloc) == 1:
            host, port = netloc[0], 80
        else:
            host, port = netloc
        return AsyncIOHTTPClient(host, port, tls, timeout, loop=loop)
    else:
        raise RuntimeError('This scheme does not supported.')
