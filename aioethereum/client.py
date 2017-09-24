import logging
import asyncio

import aiohttp
import async_timeout

try:
    import ujson as json  # noqa
except ImportError:
    import json

from .errors import BadResponseError, BadStatusError, BadJsonError
from .management import (
    DbMixin, EthMixin, NetMixin, PersonalMixin, ShhMixin, Web3Mixin)


logger = logging.getLogger('asyncio_client')


class AsyncIOClient(DbMixin, EthMixin, NetMixin, PersonalMixin,
                    ShhMixin, Web3Mixin):

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
            response = yield from r.json()
        except ValueError:
            raise BadJsonError('Invalid received json from node.')

        if not _id:
            self._id += 1
        try:
            return response['result']
        except KeyError:
            raise BadResponseError(response['error']['message'],
                                   response['error']['code'])
