from unittest import mock
import asyncio

import pytest
import aiohttp

from aioethereum.errors import BadStatusError, BadJsonError, BadResponseError


@pytest.mark.run_loop
def test_rpc_call_with_conn_error(create_ethereum_client, loop, server):
    with mock.patch("asyncio.StreamWriter.write") as write:
        write.return_value = asyncio.Future(loop=loop)
        write.return_value.set_result(None)
        with mock.patch("asyncio.StreamReader.readline") as readline:
            readline.return_value = asyncio.Future(loop=loop)
            readline.return_value.set_result(b'')

            client = yield from create_ethereum_client(server.unixsocket,
                                                       loop=loop)

            with pytest.raises(ConnectionError):
                yield from client.rpc_call('test_method')


# @pytest.mark.run_loop
# def test_rpc_call_with_bad_status(create_ethereum_client, loop, server):
#     resp = mock.Mock()
#     resp.status = 101
#     with mock.patch("aiohttp.client.ClientSession._request") as patched:
#         patched.return_value = asyncio.Future(loop=loop)
#         patched.return_value.set_result(resp)
#         client = yield from create_ethereum_client(server.http_address,
#                                                    loop=loop)
#         with pytest.raises(BadStatusError) as excinfo:
#             yield from client.rpc_call('test_method')

#         assert patched.called, "`ClientSession._request` not called"
#         assert list(patched.call_args)[0] == ('POST', server.http_address)
#         assert str(resp.status) in str(excinfo)


# @pytest.mark.run_loop
# def test_rpc_call_unmarshling_error(create_ethereum_client, loop, server):
#     resp = mock.Mock()
#     resp.status = 200
#     resp.json = mock.Mock()
#     resp.json.return_value = asyncio.Future(loop=loop)
#     resp.json.return_value.set_result(None)
#     resp.json.side_effect = ValueError('unmarshal')

#     with mock.patch("aiohttp.client.ClientSession._request") as patched:
#         patched.return_value = asyncio.Future(loop=loop)
#         patched.return_value.set_result(resp)
#         client = yield from create_ethereum_client(server.http_address,
#                                                    loop=loop)
#         with pytest.raises(BadJsonError):
#             yield from client.rpc_call('test_method')

#         assert patched.called, "`ClientSession._request` not called"
#         assert list(patched.call_args)[0] == ('POST', server.http_address)


# @pytest.mark.run_loop
# def test_rpc_call_with_bad_result(create_ethereum_client, loop, server):
#     resp = mock.Mock()
#     resp.status = 200
#     resp.json = mock.Mock()
#     resp.json.return_value = asyncio.Future(loop=loop)
#     resp.json.return_value.set_result({
#         'error': {'message': 'bad', 'code': -999999}})

#     with mock.patch("aiohttp.client.ClientSession._request") as patched:
#         patched.return_value = asyncio.Future(loop=loop)
#         patched.return_value.set_result(resp)
#         client = yield from create_ethereum_client(server.http_address,
#                                                    loop=loop)
#         with pytest.raises(BadResponseError) as excinfo:
#             yield from client.rpc_call('test_method')

#         assert patched.called, "`ClientSession._request` not called"
#         assert list(patched.call_args)[0] == ('POST', server.http_address)
#         assert -999999 == excinfo.value.code
#         assert 'bad' == excinfo.value.msg
