from collections import Mapping

import pytest

from aioethereum.errors import BadResponseError


@pytest.mark.run_loop
def test_call_admin_addPeer(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.admin_addPeer(
        'enode://44826a5d6a55f88a18298bca4773fca5749cdc3a5c9f308aa7d810e9b31123f3e7c5fba0b1d70aac5308426f47df2a128a6747040a3815cc7dd7167d03be320d@[::]:30303')  # noqa
    assert isinstance(response, bool)


@pytest.mark.run_loop
def test_call_admin_datadir(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.admin_datadir()
    assert response == server.dir


@pytest.mark.run_loop
def test_call_admin_nodeInfo(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.admin_nodeInfo()
    assert isinstance(response, Mapping)


@pytest.mark.run_loop
def test_call_admin_peers(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.admin_peers()
    assert isinstance(response, list)


@pytest.mark.run_loop
def test_call_admin_setSolc(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    with pytest.raises(BadResponseError) as excinfo:
        yield from client.admin_setSolc()

    assert excinfo.value.code == -32601
    assert 'does not exist/is not available' in excinfo.value.msg


@pytest.mark.run_loop
def test_call_admin_startRPC(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    with pytest.raises(BadResponseError) as excinfo:
        yield from client.admin_startRPC()

    assert excinfo.value.code == -32000
    assert 'HTTP RPC already running' in excinfo.value.msg


@pytest.mark.run_loop
def test_call_admin_startWS(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    with pytest.raises(BadResponseError) as excinfo:
        yield from client.admin_startWS()

    assert excinfo.value.code == -32000
    assert 'WebSocket RPC already running' in excinfo.value.msg


@pytest.mark.run_loop
@pytest.mark.skip(reason='stops rpc channel, don\'t know what to do yet')
def test_call_admin_stopRPC(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.admin_stopRPC()
    assert isinstance(response, bool)

    yield from client.admin_startRPC(server.host, server.rpcport, '*',
                                     server.apis)


@pytest.mark.run_loop
@pytest.mark.skip(reason='stops ws channel, don\'t know what to do yet')
def test_call_admin_stopWS(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.admin_stopWS()
    assert isinstance(response, bool)

    yield from client.admin_startWS(server.host, server.wsport, '*',
                                    server.apis)
