import pytest


@pytest.mark.run_loop
def test_call_eth_protocolVersion(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.eth_protocolVersion()
    assert isinstance(response, int)


@pytest.mark.run_loop
def test_call_eth_syncing(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.eth_syncing()
    assert response is False


@pytest.mark.run_loop
def test_call_eth_coinbase(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.eth_coinbase()
    assert response == server.coinbase


@pytest.mark.run_loop
def test_call_eth_mining(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.eth_mining()
    assert isinstance(response, bool)


@pytest.mark.run_loop
def test_call_eth_hashrate(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.eth_hashrate()
    assert isinstance(response, int)


@pytest.mark.run_loop
def test_call_eth_gasPrice(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.eth_gasPrice()
    assert isinstance(response, int)


@pytest.mark.run_loop
def test_call_eth_accounts(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.eth_accounts()
    assert isinstance(response, list)


@pytest.mark.run_loop
def test_call_eth_blockNumber(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.eth_blockNumber()
    assert isinstance(response, int)


@pytest.mark.run_loop
def test_call_eth_getBalance(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.eth_getBalance(server.coinbase)
    assert isinstance(response, int)


@pytest.mark.run_loop
def test_call_eth_getStorageAt(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.eth_getStorageAt(server.coinbase)
    assert isinstance(response, int)


@pytest.mark.run_loop
def test_call_eth_getTransactionCount(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.eth_getTransactionCount(server.coinbase)
    assert isinstance(response, int)


@pytest.mark.run_loop
def test_call_eth_getBlockTransactionCountByHash(create_ethereum_client, loop,
                                                 server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.eth_getBlockTransactionCountByHash(
        '0xb903239f8543d04b5dc1ba6579132b143087c68db1b2168786408fcbce568238')
    assert response is None


@pytest.mark.run_loop
def test_call_eth_getBlockTransactionCountByNumber(create_ethereum_client,
                                                   loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.eth_getBlockTransactionCountByNumber()
    assert isinstance(response, int)


@pytest.mark.run_loop
def test_call_eth_getUncleCountByBlockHash(create_ethereum_client, loop,
                                           server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.eth_getUncleCountByBlockHash(
        '0xb903239f8543d04b5dc1ba6579132b143087c68db1b2168786408fcbce568238')
    assert response is None
