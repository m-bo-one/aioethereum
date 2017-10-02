import pytest


@pytest.mark.run_loop
def test_call_net_version(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.net_version()
    assert isinstance(response, str)


@pytest.mark.run_loop
def test_call_net_listening(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.net_listening()
    assert isinstance(response, bool)


@pytest.mark.run_loop
def test_call_net_peerCount(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.net_peerCount()
    assert isinstance(response, int)
