import os
import re
import time
import socket
import asyncio
import subprocess
from collections import namedtuple
from urllib.request import urlopen
from urllib.error import URLError

import pytest
import aioethereum


NodeServer = namedtuple('NodeServer',
                        ('dir unixsocket http_address ws_address coinbase '
                         'host rpcport wsport apis'))


@pytest.fixture(scope='session')
def unused_port():
    """Gets random free port."""
    def fun():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('127.0.0.1', 0))
            return s.getsockname()[1]
    return fun


@pytest.fixture
def loop():
    """Creates new event loop."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(None)

    try:
        yield loop
    finally:
        if hasattr(loop, 'is_closed'):
            closed = loop.is_closed()
        else:
            closed = loop._closed   # XXX
        if not closed:
            loop.call_soon(loop.stop)
            loop.run_forever()
            loop.close()


@pytest.fixture
def create_ethereum_client(loop):
    """Wrapper around aioethereum.create_ethereum_client."""

    @asyncio.coroutine
    def f(*args, **kw):
        kw.setdefault('loop', loop)
        client = yield from aioethereum.create_ethereum_client(*args, **kw)
        return client
    return f


@pytest.fixture(scope='session')
def server(unused_port):
    try:
        node_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                'node')
        unix_domain_path = 'unix://%s' % os.path.join(node_dir, 'testnet',
                                                      'geth.ipc')
        host, port, wsport = ('localhost', unused_port(), unused_port())
        node_port = unused_port()
        apis = ['eth', 'web3', 'net', 'personal', 'db', 'shh', 'txpool',
                'miner', 'admin', 'debug']

        process = subprocess.Popen(['make', '-C', node_dir, 'start',
                                    'HOST=%s' % host,
                                    'NODE_PORT=%s' % node_port,
                                    'RPC_PORT=%s' % port,
                                    'WS_PORT=%s' % wsport,
                                    'APIS=%s' % ','.join(apis)],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        stdout, _ = process.communicate()
        assert process.returncode == 0, stdout.decode('utf-8')

        base_uri = 'http://%s:%s' % (host, port)
        ws_uri = 'http://%s:%s' % (host, wsport)
        tried = 0
        max_tries = 5
        while tried < max_tries:
            try:
                urlopen(base_uri)
                break
            except URLError:
                tried += 1
                print('\nWaiting for node connection, max tries left: %d' %
                      (max_tries - tried))
                time.sleep(1)

        assert tried != max_tries, 'Node not started on %s' % base_uri

        process = subprocess.Popen(['make', '-C', node_dir, 'waitmoney'],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        stdout, _ = process.communicate()

        process = subprocess.Popen(['make', '-C', node_dir, 'coinbase'],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        stdout, _ = process.communicate()

        print('\nNode started at %s' % base_uri)

        coinbase = re.search(r'\"(.*?)\"', stdout.decode('utf-8')).group(1)
        server = NodeServer(os.path.join(node_dir, 'testnet'),
                            unix_domain_path, base_uri, ws_uri, coinbase,
                            host, port, wsport, apis)
        yield server
    finally:
        process = subprocess.Popen(['make', '-C', node_dir, 'stop'],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        process.wait()
        process = subprocess.Popen(['make', '-C', node_dir, 'destroy'],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        process.wait()


@pytest.mark.tryfirst
def pytest_pycollect_makeitem(collector, name, obj):
    if collector.funcnamefilter(name):
        if not callable(obj):
            return
        item = pytest.Function(name, parent=collector)
        if 'run_loop' in item.keywords:
            # TODO: re-wrap with asyncio.coroutine if not native coroutine
            return list(collector._genfunctions(name, obj))


@pytest.mark.tryfirst
def pytest_pyfunc_call(pyfuncitem):
    """
    Run asyncio marked test functions in an event loop instead of a normal
    function call.
    """
    if 'run_loop' in pyfuncitem.keywords:
        funcargs = pyfuncitem.funcargs
        loop = funcargs['loop']
        testargs = {arg: funcargs[arg]
                    for arg in pyfuncitem._fixtureinfo.argnames}

        loop.run_until_complete(pyfuncitem.obj(**testargs))
        return True


def pytest_runtest_setup(item):
    if 'run_loop' in item.keywords and 'loop' not in item.fixturenames:
        # inject an event loop fixture for all async tests
        item.fixturenames.append('loop')
