import pytest

from aioethereum.errors import BadResponseError


@pytest.mark.run_loop
def test_call_shh_version(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.shh_version()
    assert isinstance(response, float)


@pytest.mark.run_loop
@pytest.mark.skip(reason='incorect datatypes in RPC API, not worked now')
def test_call_shh_post(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.shh_post("""FIXME""")
    assert response is False


@pytest.mark.run_loop
def test_call_shh_newIdentity(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    with pytest.raises(BadResponseError) as excinfo:
        yield from client.shh_newIdentity()

    assert excinfo.value.code == -32601
    assert 'does not exist/is not available' in excinfo.value.msg


@pytest.mark.run_loop
def test_call_shh_hasIdentity(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    with pytest.raises(BadResponseError) as excinfo:
        yield from client.shh_hasIdentity(
            '0x08fcff507b9eda1de5a7b10f593606a998ab75ad')

    assert excinfo.value.code == -32601
    assert 'does not exist/is not available' in excinfo.value.msg


@pytest.mark.run_loop
def test_call_shh_newGroup(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    with pytest.raises(BadResponseError) as excinfo:
        yield from client.shh_newGroup()

    assert excinfo.value.code == -32601
    assert 'does not exist/is not available' in excinfo.value.msg


@pytest.mark.run_loop
def test_call_shh_addToGroup(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    with pytest.raises(BadResponseError) as excinfo:
        yield from client.shh_addToGroup()

    assert excinfo.value.code == -32601
    assert 'does not exist/is not available' in excinfo.value.msg


@pytest.mark.run_loop
def test_call_shh_newFilter(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    with pytest.raises(BadResponseError) as excinfo:
        yield from client.shh_newFilter(topics=['0xb'])

    assert excinfo.value.code == -32601
    assert 'does not exist/is not available' in excinfo.value.msg


@pytest.mark.run_loop
def test_call_shh_uninstallFilter(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    with pytest.raises(BadResponseError) as excinfo:
        yield from client.shh_uninstallFilter('0xb')

    assert excinfo.value.code == -32601
    assert 'does not exist/is not available' in excinfo.value.msg


@pytest.mark.run_loop
def test_call_shh_getFilterChanges(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    with pytest.raises(BadResponseError) as excinfo:
        yield from client.shh_getFilterChanges('0xb')

    assert excinfo.value.code == -32601
    assert 'does not exist/is not available' in excinfo.value.msg


@pytest.mark.run_loop
def test_call_shh_getMessages(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    with pytest.raises(BadResponseError) as excinfo:
        yield from client.shh_getMessages('0xb')

    assert excinfo.value.code == -32601
    assert 'does not exist/is not available' in excinfo.value.msg
