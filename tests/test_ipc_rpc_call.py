import sys
from unittest import mock
import asyncio

import pytest

from aioethereum.errors import BadJsonError, BadResponseError


@pytest.mark.run_loop
@pytest.mark.skipif(sys.platform == 'win32',
                    reason='No unixsocket on Windows')
def test_rpc_call_with_conn_error(create_ethereum_client, loop, server):
    with mock.patch("asyncio.StreamWriter.write") as write:
        write.return_value = asyncio.Future(loop=loop)
        write.return_value.set_result(None)
        with mock.patch("asyncio.StreamReader.readline") as readline:
            readline.return_value = asyncio.Future(loop=loop)
            readline.return_value.set_result(b'')

            client = yield from create_ethereum_client(server.unixsocket,
                                                       loop=loop)

            with mock.patch("aioethereum.client.create_ethereum_client") as cc:
                cc.return_value = asyncio.Future(loop=loop)
                cc.side_effect = ConnectionError('error')
                cc.return_value.set_result(None)

                with pytest.raises(ConnectionError):
                    yield from client.rpc_call('test_method')


@pytest.mark.run_loop
@pytest.mark.skipif(sys.platform == 'win32',
                    reason='No unixsocket on Windows')
def test_rpc_call_unmarshling_error(create_ethereum_client, loop, server):
    with mock.patch("asyncio.StreamWriter.write") as write:
        write.return_value = asyncio.Future(loop=loop)
        write.return_value.set_result(None)
        with mock.patch("asyncio.StreamReader.readline") as readline:
            readline.return_value = asyncio.Future(loop=loop)
            readline.return_value.set_result(b'{"fe": 32235235')

            client = yield from create_ethereum_client(server.unixsocket,
                                                       loop=loop)

            with pytest.raises(BadJsonError):
                yield from client.rpc_call('test_method')


@pytest.mark.run_loop
@pytest.mark.skipif(sys.platform == 'win32',
                    reason='No unixsocket on Windows')
def test_rpc_call_with_bad_result(create_ethereum_client, loop, server):
    with mock.patch("asyncio.StreamWriter.write") as write:
        write.return_value = asyncio.Future(loop=loop)
        write.return_value.set_result(None)
        with mock.patch("asyncio.StreamReader.readline") as readline:
            readline.return_value = asyncio.Future(loop=loop)
            readline.return_value.set_result(
                b'{"error": {"code": -99999, "message": "error"}}\n')

            client = yield from create_ethereum_client(server.unixsocket,
                                                       loop=loop)

            with pytest.raises(BadResponseError):
                yield from client.rpc_call('test_method')
