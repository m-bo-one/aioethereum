import asyncio


class MinerMixin:

    @asyncio.coroutine
    def miner_setExtra(self, data):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#miner_setextra

        :param data: Extra data a miner can include when miner blocks
        :type data: str

        :rtype: bool
        """
        return (yield from self.rpc_call('miner_setExtra', [data]))

    @asyncio.coroutine
    def miner_setGasPrice(self, number):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#miner_setgasprice

        :param number: Minimal accepted gas price when mining transactions
        :type number: int

        :rtype: bool
        """
        return (yield from self.rpc_call('miner_setGasPrice', [hex(number)]))

    @asyncio.coroutine
    def miner_start(self, number):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#miner_start

        :param number: CPU mining process with the given number of threads
        :type number: int

        :rtype: None
        """
        return (yield from self.rpc_call('miner_start', [number]))

    @asyncio.coroutine
    def miner_stop(self):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#miner_stop

        :rtype: bool
        """
        return (yield from self.rpc_call('miner_stop'))

    @asyncio.coroutine
    def miner_setEtherBase(self, address):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#miner_setetherbase

        NOT AVAILABLE
        """
        return (yield from self.rpc_call('miner_setEtherBase', [address]))
