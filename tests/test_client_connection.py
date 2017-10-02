import sys
import asyncio
import pytest

import aioethereum


def test_global_loop(create_ethereum_client, loop, server):
    asyncio.set_event_loop(loop)

    client = loop.run_until_complete(create_ethereum_client(
        server.http_address, loop=loop))
    assert client._host in server.http_address
    assert client._port in server.http_address
    assert client._loop is loop


@pytest.mark.run_loop
@pytest.mark.skipif(sys.platform == 'win32',
                    reason='No unixsocket on Windows')
def test_connect_unixsocket(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.unixsocket,
                                               loop=loop)
    assert isinstance(client, aioethereum.AsyncIOIPCClient)

    reader, writer = client._reader, client._writer
    assert isinstance(reader, asyncio.StreamReader)
    assert isinstance(writer, asyncio.StreamWriter)

    assert client._unix_path == server.unixsocket
