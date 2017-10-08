from collections import Mapping
import pytest

from aioethereum.errors import BadResponseError
from aioethereum.utils import add_0x


@pytest.mark.run_loop
def test_call_debug_backtraceAt(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.debug_backtraceAt('server.go:443')
    assert response is None


@pytest.mark.run_loop
def test_call_debug_blockProfile(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.debug_blockProfile('/dev/null', 0)
    assert response is None


@pytest.mark.run_loop
def test_call_debug_cpuProfile(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.debug_cpuProfile('/dev/null', 0)
    assert response is None


@pytest.mark.run_loop
def test_call_debug_dumpBlock(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.debug_dumpBlock(1)
    assert isinstance(response, Mapping)


@pytest.mark.run_loop
def test_call_debug_gcStats(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.debug_gcStats()
    assert isinstance(response, Mapping)


@pytest.mark.run_loop
def test_call_debug_getBlockRlp(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.debug_getBlockRlp(0)
    assert isinstance(response, str)


@pytest.mark.run_loop
def test_call_debug_goTrace(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.debug_goTrace('/dev/null', 0)
    assert response is None


@pytest.mark.run_loop
@pytest.mark.skip(reason='don\'t answer allways')
def test_call_debug_memStats(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.debug_memStats()
    assert isinstance(response, Mapping)


@pytest.mark.run_loop
def test_call_debug_seedHash(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.debug_seedHash(1)
    assert isinstance(response, str)


@pytest.mark.run_loop
def test_call_debug_setHead(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.debug_setHead(1)
    assert response is None


@pytest.mark.run_loop
def test_call_debug_setBlockProfileRate(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.debug_setBlockProfileRate(1)
    assert response is None


@pytest.mark.run_loop
@pytest.mark.skip(reason='don\'t answer allways')
def test_call_debug_stacks(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.debug_stacks()
    assert isinstance(response, str)


@pytest.mark.run_loop
def test_call_debug_startCPUProfile(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.debug_startCPUProfile('/dev/null')
    assert response is None


@pytest.mark.run_loop
def test_call_debug_startGoTrace(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.debug_startGoTrace('/dev/null')
    assert response is None


@pytest.mark.run_loop
def test_call_debug_stopCPUProfile(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.debug_stopCPUProfile()
    assert response is None


@pytest.mark.run_loop
def test_call_debug_stopGoTrace(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.debug_stopGoTrace()
    assert response is None


@pytest.mark.run_loop
def test_call_debug_traceBlock(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.debug_traceBlock([])
    assert isinstance(response, Mapping)


@pytest.mark.run_loop
def test_call_debug_traceBlockByNumber(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.debug_traceBlockByNumber(1)
    assert isinstance(response, Mapping)


@pytest.mark.run_loop
def test_call_debug_traceBlockByHash(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.debug_traceBlockByHash(
        "0x5d6f025c93ef5432c58af082ff3d5719469ad2e65f87801b14d8d29da415d208")
    assert isinstance(response, Mapping)


@pytest.mark.run_loop
def test_call_debug_traceBlockFromFile(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.debug_traceBlockFromFile('/dev/null')
    assert isinstance(response, Mapping)


@pytest.mark.run_loop
def test_call_debug_traceTransaction(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    txhash = '5d6f025c93ef5432c58af082ff3d5719469ad2e65f87801b14d8d29da415d208'  # noqa
    with pytest.raises(BadResponseError) as excinfo:
        yield from client.debug_traceTransaction(add_0x(txhash))

    assert excinfo.value.code == -32000
    assert 'transaction %s not found' % txhash == excinfo.value.msg


@pytest.mark.run_loop
def test_call_debug_verbosity(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.debug_verbosity(1)
    assert response is None


@pytest.mark.run_loop
def test_call_debug_vmodule(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.debug_vmodule("eth/*=6")
    assert response is None


@pytest.mark.run_loop
def test_call_debug_writeBlockProfile(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.debug_writeBlockProfile('/dev/null')
    assert response is None


@pytest.mark.run_loop
def test_call_debug_writeMemProfile(create_ethereum_client, loop, server):
    client = yield from create_ethereum_client(server.http_address,
                                               loop=loop)
    response = yield from client.debug_writeMemProfile('/dev/null')
    assert response is None
