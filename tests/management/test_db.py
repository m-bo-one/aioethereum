import pytest

from aioethereum.errors import BadResponseError


@pytest.mark.run_loop
def test_call_db_putString(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    with pytest.raises(BadResponseError) as excinfo:
        yield from client.db_putString('baza', 'vitalika', 'kefirika')

    assert excinfo.value.code == -32601
    assert 'does not exist/is not available' in excinfo.value.msg


@pytest.mark.run_loop
def test_call_db_getString(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    with pytest.raises(BadResponseError) as excinfo:
        yield from client.db_getString('baza', 'kidalika')

    assert excinfo.value.code == -32601
    assert 'does not exist/is not available' in excinfo.value.msg


@pytest.mark.run_loop
def test_call_db_putHex(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    with pytest.raises(BadResponseError) as excinfo:
        yield from client.db_putHex('baza', 'vitalika', 'kefirika')

    assert excinfo.value.code == -32601
    assert 'does not exist/is not available' in excinfo.value.msg


@pytest.mark.run_loop
def test_call_db_getHex(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    with pytest.raises(BadResponseError) as excinfo:
        yield from client.db_getHex('baza', 'kidalika')

    assert excinfo.value.code == -32601
    assert 'does not exist/is not available' in excinfo.value.msg
