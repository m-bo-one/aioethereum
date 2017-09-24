import asyncio


class MinerMixin:

    @asyncio.coroutine
    def miner_setExtra(self, data):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#miner_setextra
        """
        result = yield from self._call('miner_setExtra', [data])
        return result

    @asyncio.coroutine
    def miner_setGasPrice(self, number):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#miner_setgasprice
        """
        result = yield from self._call('miner_setGasPrice', [hex(number)])
        return result

    @asyncio.coroutine
    def miner_start(self, number):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#miner_start
        """
        result = yield from self._call('miner_start', [number])
        return result

    @asyncio.coroutine
    def miner_stop(self):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#miner_stop
        """
        result = yield from self._call('miner_stop')
        return result

    @asyncio.coroutine
    def miner_setEtherBase(self, address):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#miner_setetherbase
        N/A
        """
        result = yield from self._call('miner_setEtherBase', [address])
        return result
