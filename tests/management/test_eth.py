from collections import Mapping
import pytest

from aioethereum.errors import BadResponseError


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


@pytest.mark.run_loop
def test_call_eth_getUncleCountByBlockNumber(create_ethereum_client, loop,
                                             server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.eth_getUncleCountByBlockNumber()
    assert response == 0


@pytest.mark.run_loop
def test_call_eth_getCode(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.eth_getCode(server.coinbase)
    assert response == '0x'


@pytest.mark.run_loop
def test_call_eth_sign(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)

    yield from client.personal_unlockAccount(server.coinbase)
    response = yield from client.eth_sign(server.coinbase, '0xdeadbeaf')
    assert isinstance(response, str)
    yield from client.personal_lockAccount(server.coinbase)


@pytest.mark.run_loop
def test_call_eth_sendTransaction(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    yield from client.personal_unlockAccount(server.coinbase)
    response = yield from client.eth_sendTransaction(
        from_=server.coinbase,
        to='0x08fcff507b9eda1de5a7b10f593606a998ab75ad',
        gas=31000,
        gas_price=1 * 10**9,
        value=0.001,
        data='0xc0de',
        nonce=2)
    assert isinstance(response, str)

    response = yield from client.eth_sendTransaction(server.coinbase)
    assert isinstance(response, str)
    yield from client.personal_lockAccount(server.coinbase)


@pytest.mark.run_loop
def test_call_eth_sendRawTransaction(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    with pytest.raises(BadResponseError) as excinfo:
        yield from client.eth_sendRawTransaction('')
    assert excinfo.value.code == -32000


@pytest.mark.run_loop
def test_call_eth_call(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    yield from client.personal_unlockAccount(server.coinbase)
    response = yield from client.eth_call(
        from_=server.coinbase,
        to='0x08fcff507b9eda1de5a7b10f593606a998ab75ad',
        gas=31000,
        gas_price=1 * 10**9,
        value=0.001,
        data='0xc0de')
    assert isinstance(response, str)


@pytest.mark.run_loop
def test_call_eth_estimateGas(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    yield from client.personal_unlockAccount(server.coinbase)
    response = yield from client.eth_estimateGas(
        from_=server.coinbase,
        to='0x08fcff507b9eda1de5a7b10f593606a998ab75ad',
        gas=31000,
        gas_price=1 * 10**9,
        value=0.001,
        data='0xc0de')
    assert isinstance(response, int)


@pytest.mark.run_loop
def test_call_eth_getBlockByHash(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    yield from client.personal_unlockAccount(server.coinbase)
    response = yield from client.eth_getBlockByHash(
        '0x850c6fb78d9627e9701f225e02357ae69fb2cd147f2f12a6663251f35ff6ff35')
    assert response is None


@pytest.mark.run_loop
def test_call_eth_getBlockByNumber(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    yield from client.personal_unlockAccount(server.coinbase)
    response = yield from client.eth_getBlockByNumber()
    assert isinstance(response, Mapping)


@pytest.mark.run_loop
def test_call_eth_getTransactionByHash(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    yield from client.personal_unlockAccount(server.coinbase)
    response = yield from client.eth_getTransactionByHash(
        '0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347')
    assert response is None


@pytest.mark.run_loop
def test_call_eth_getTransactionByBlockHashAndIndex(create_ethereum_client,
                                                    loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    yield from client.personal_unlockAccount(server.coinbase)
    response = yield from client.eth_getTransactionByBlockHashAndIndex(
        '0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347')
    assert response is None
