import pytest


@pytest.mark.run_loop
def test_call_personal_importRawKey(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.personal_importRawKey(
        '01e389e46bb9e0abf3c4f661fda97b5e6595d525b4f8a68a809fe352b0790c75',
        'qwerty123')
    assert response == '0x3d6d942574d6ac9aa9d9963ab242969276810e64'


@pytest.mark.run_loop
def test_call_personal_listAccounts(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.personal_listAccounts()
    assert isinstance(response, list)


@pytest.mark.run_loop
def test_call_personal_lockAccount(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.personal_lockAccount(
        '0x08fcff507b9eda1de5a7b10f593606a998ab75ad')
    assert response is True


@pytest.mark.run_loop
def test_call_personal_newAccount(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.personal_newAccount()
    assert isinstance(response, str)


@pytest.mark.run_loop
def test_call_personal_unlockAccount(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.personal_unlockAccount(server.coinbase, None)
    assert response is True


@pytest.mark.run_loop
def test_call_personal_sendTransaction(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.personal_sendTransaction(
        from_=server.coinbase,
        to='0x08fcff507b9eda1de5a7b10f593606a998ab75ad',
        gas=31000,
        gas_price=1 * 10**9,
        value=0.001,
        data='0xc0de',
        nonce=1)
    assert isinstance(response, str)

    response = yield from client.personal_sendTransaction(server.coinbase)
    assert isinstance(response, str)


@pytest.mark.run_loop
def test_call_personal_sign(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.personal_sign(
        '0xdeadbeaf', server.coinbase, None)
    assert isinstance(response, str)


@pytest.mark.run_loop
def test_call_personal_ecRecover(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.personal_ecRecover(
        '0xdeadbeaf',
        '0x0ecbf5d5179f7ba44f74fd16f6b25ecc4e0688908800b582a8578e953164816457111557beb8b9d2a2006d1cd57c52ee9c18d3f0c8c49e2dbd5ccf23bc3ef57a1b')  # noqa
    assert isinstance(response, str)
