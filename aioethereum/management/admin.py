import asyncio


class AdminMixin:

    @asyncio.coroutine
    def admin_addPeer(self, url):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#admin_addpeer

        :param url: Enode url of peer
        :type url: str

        :rtype: bool
        """
        return (yield from self.rpc_call('admin_addPeer', [url]))

    @asyncio.coroutine
    def admin_datadir(self):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#admin_datadir

        :return: path
        :rtype: str
        """
        return (yield from self.rpc_call('admin_datadir'))

    @asyncio.coroutine
    def admin_nodeInfo(self):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#admin_nodeinfo

        :return: info
        :rtype: dict
        """
        return (yield from self.rpc_call('admin_nodeInfo'))

    @asyncio.coroutine
    def admin_peers(self):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#admin_peers

        :return: info
        :rtype: list
        """
        return (yield from self.rpc_call('admin_peers'))

    @asyncio.coroutine
    def admin_setSolc(self, path='/usr/bin/solc'):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#admin_setsolc

        NOT AVAILABLE
        """
        return (yield from self.rpc_call('admin_setSolc', [path]))

    @asyncio.coroutine
    def admin_startRPC(self, host='localhost', port=8545, cors=None, apis=None):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#admin_startrpc

        :param host: Network interface to open the listener socket (optional)
        :type host: str

        :param port: Network port to open the listener socket (optional)
        :type port: int

        :param cors: Cross-origin resource sharing header to use (optional)
        :type cors: str

        :param apis: API modules to offer over this interface (optional)
        :type apis: str

        :rtype: bool
        """
        if cors is None:
            cors = []
        if apis is None:
            apis = ['eth', 'net', 'web3']

        return (yield from self.rpc_call('admin_startRPC',
                                         [host, port,
                                          ','.join(cors), ','.join(apis)]))

    @asyncio.coroutine
    def admin_startWS(self, host='localhost', port=8546, cors=None, apis=None):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#admin_startws

        :param host: Network interface to open the listener socket (optional)
        :type host: str

        :param port: Network port to open the listener socket (optional)
        :type port: int

        :param cors: Cross-origin resource sharing header to use (optional)
        :type cors: str

        :param apis: API modules to offer over this interface (optional)
        :type apis: str

        :rtype: bool
        """
        if cors is None:
            cors = []
        if apis is None:
            apis = ['eth', 'net', 'web3']

        return (yield from self.rpc_call('admin_startWS',
                                         [host, port,
                                          ','.join(cors), ','.join(apis)]))

    @asyncio.coroutine
    def admin_stopRPC(self):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#admin_stoprpc

        :rtype: bool
        """
        return (yield from self.rpc_call('admin_stopRPC'))

    @asyncio.coroutine
    def admin_stopWS(self):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#admin_stopws

        :rtype: bool
        """
        return (yield from self.rpc_call('admin_stopWS'))
