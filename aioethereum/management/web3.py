import asyncio
import binascii

from ..utils import add_0x


class Web3Mixin:

    @asyncio.coroutine
    def web3_clientVersion(self):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#web3_clientversion
        """
        result = yield from self._call('web3_clientVersion')
        return result

    @asyncio.coroutine
    def web3_sha3(self, data):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#web3_sha3
        """
        data = add_0x(binascii.hexlify(str(data).encode('utf-8')))
        result = yield from self._call('web3_sha3', [data])
        return result
