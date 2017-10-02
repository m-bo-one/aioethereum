import pytest

from aioethereum.errors import BadResponseError


@pytest.mark.run_loop
def test_call_miner_setExtra(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.miner_setExtra('Papa ne mayni!')
    assert response is True


@pytest.mark.run_loop
def test_call_miner_setGasPrice(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.miner_setGasPrice(4000000000)
    assert response is True


@pytest.mark.run_loop
def test_call_miner_start(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.miner_start(1)
    assert response is None


@pytest.mark.run_loop
def test_call_miner_stop(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.miner_stop()
    assert response is True


@pytest.mark.run_loop
def test_call_miner_setEtherBase(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    with pytest.raises(BadResponseError) as excinfo:
        yield from client.miner_setEtherBase(
            '0x08fcff507b9eda1de5a7b10f593606a998ab75ad')

    assert excinfo.value.code == -32601
    assert 'does not exist/is not available' in excinfo.value.msg
