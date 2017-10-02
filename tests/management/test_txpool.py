from collections import Mapping

import pytest


@pytest.mark.run_loop
def test_call_txpool_content(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.txpool_content()
    assert isinstance(response, Mapping)


@pytest.mark.run_loop
def test_call_txpool_inspect(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.txpool_inspect()
    assert isinstance(response, Mapping)


@pytest.mark.run_loop
def test_call_txpool_status(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.txpool_status()
    assert isinstance(response, Mapping)
