import pytest


@pytest.mark.run_loop
def test_call_web3_clientVersion(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.web3_clientVersion()
    assert isinstance(response, str)


@pytest.mark.run_loop
def test_call_web3_sha3(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.web3_sha3('0x0')
    assert isinstance(response, str)
