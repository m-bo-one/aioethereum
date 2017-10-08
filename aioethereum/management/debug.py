import asyncio


class DebugMixin:

    @asyncio.coroutine
    def debug_backtraceAt(self, filename_line):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#debug_backtraceat

        :param filename_line: Filename and its line for debugging
        :type filename_line: str

        :rtype: None
        """
        return (yield from self.rpc_call('debug_backtraceAt', [filename_line]))

    @asyncio.coroutine
    def debug_blockProfile(self, file, seconds):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#debug_blockprofile

        :param file: Log file path
        :type file: str

        :param seconds: Seconds for profile capturing
        :type seconds: int

        :rtype: None
        """
        return (yield from self.rpc_call('debug_blockProfile', [file, seconds]))

    @asyncio.coroutine
    def debug_cpuProfile(self, file, seconds):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#debug_cpuprofile

        :param file: Log file path
        :type file: str

        :param seconds: Seconds for profile capturing
        :type seconds: int

        :rtype: None
        """
        return (yield from self.rpc_call('debug_cpuProfile', [file, seconds]))

    @asyncio.coroutine
    def debug_dumpBlock(self, number):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#debug_dumpblock

        :param number: Block number
        :type number: int

        :return: accounts
        :rtype: dict
        """
        return (yield from self.rpc_call('debug_dumpBlock', [hex(number)]))

    @asyncio.coroutine
    def debug_gcStats(self):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#debug_gcstats

        :return: https://golang.org/pkg/runtime/debug/#GCStats
        :rtype: dict
        """
        return (yield from self.rpc_call('debug_gcStats'))

    @asyncio.coroutine
    def debug_getBlockRlp(self, number):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#debug_getblockrlp

        :param number: Block number
        :type number: int

        :return: RLP
        :rtype: str
        """
        return (yield from self.rpc_call('debug_getBlockRlp', [number]))

    @asyncio.coroutine
    def debug_goTrace(self, file, seconds):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#debug_gotrace

        :param file: Log file path
        :type file: str

        :param seconds: Seconds for profile capturing
        :type seconds: int

        :rtype: None
        """
        return (yield from self.rpc_call('debug_goTrace', [file, seconds]))

    @asyncio.coroutine
    def debug_memStats(self):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#debug_memstats

        :return: https://golang.org/pkg/runtime/debug/#MemStats
        :rtype: dict
        """
        return (yield from self.rpc_call('debug_memStats'))

    @asyncio.coroutine
    def debug_seedHash(self, number):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#debug_seedhash

        :param number: Block number
        :type number: int

        :return: hash
        :rtype: str or error
        """
        return (yield from self.rpc_call('debug_seedHash', [number]))

    @asyncio.coroutine
    def debug_setHead(self, number):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#debug_sethead

        :param number: Block number
        :type number: int

        :rtype: None
        """
        return (yield from self.rpc_call('debug_setHead', [hex(number)]))

    @asyncio.coroutine
    def debug_setBlockProfileRate(self, rate):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#debug_sethead

        :param rate: Rate of goroutine block (samples/sec)
        :type rate: int

        :rtype: None
        """
        return (yield from self.rpc_call('debug_setBlockProfileRate', [rate]))

    @asyncio.coroutine
    def debug_stacks(self):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#debug_stacks

        :rtype: str
        """
        return (yield from self.rpc_call('debug_stacks'))

    @asyncio.coroutine
    def debug_startCPUProfile(self, file):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#debug_startcpuprofile

        :param file: Log file path
        :type file: str

        :rtype: None
        """
        return (yield from self.rpc_call('debug_startCPUProfile', [file]))

    @asyncio.coroutine
    def debug_startGoTrace(self, file):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#debug_startgotrace

        :param file: Log file path
        :type file: str

        :rtype: None
        """
        return (yield from self.rpc_call('debug_startGoTrace', [file]))

    @asyncio.coroutine
    def debug_stopCPUProfile(self):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#debug_stopcpuprofile

        :rtype: None
        """
        return (yield from self.rpc_call('debug_stopCPUProfile'))

    @asyncio.coroutine
    def debug_stopGoTrace(self):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#debug_stopgotrace

        :rtype: None
        """
        return (yield from self.rpc_call('debug_stopGoTrace'))

    @asyncio.coroutine
    def debug_traceBlock(self, block_rlp):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#debug_traceblock

        # TODO: Add more description for params

        :rtype: dict
        """
        return (yield from self.rpc_call('debug_traceBlock', [block_rlp]))

    @asyncio.coroutine
    def debug_traceBlockByNumber(self, number):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#debug_traceblockbynumber

        :param number: Block number
        :type number: int

        :rtype: dict
        """
        return (yield from self.rpc_call('debug_traceBlockByNumber',
                                         [hex(number)]))

    @asyncio.coroutine
    def debug_traceBlockByHash(self, bhash):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#debug_traceblockbyhash

        :param bhash: Block hash
        :type bhash: str

        :rtype: dict
        """
        return (yield from self.rpc_call('debug_traceBlockByHash', [bhash]))

    @asyncio.coroutine
    def debug_traceBlockFromFile(self, file):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#debug_traceblockfromfile

        :param file: Log file path
        :type file: str

        :rtype: dict
        """
        return (yield from self.rpc_call('debug_traceBlockFromFile', [file]))

    @asyncio.coroutine
    def debug_traceTransaction(self, txhash):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#debug_tracetransaction

        :param txhash: Transaction hash
        :type txhash: str

        :rtype: dict
        """
        return (yield from self.rpc_call('debug_traceTransaction', [txhash]))

    @asyncio.coroutine
    def debug_verbosity(self, level):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#debug_verbosity

        :param level: Debug lvl
        :type level: int

        :rtype: None
        """
        return (yield from self.rpc_call('debug_verbosity', [level]))

    @asyncio.coroutine
    def debug_vmodule(self, pattern):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#debug_vmodule

        :param pattern: Logging verbosity pattern
        :type pattern: str

        :rtype: None
        """
        return (yield from self.rpc_call('debug_vmodule', [pattern]))

    @asyncio.coroutine
    def debug_writeBlockProfile(self, file):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#debug_writeblockprofile

        :param file: Log file path
        :type file: str

        :rtype: None
        """
        return (yield from self.rpc_call('debug_writeBlockProfile', [file]))

    @asyncio.coroutine
    def debug_writeMemProfile(self, file):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#debug_writememprofile

        :param file: Log file path
        :type file: str

        :rtype: None
        """
        return (yield from self.rpc_call('debug_writeMemProfile', [file]))
