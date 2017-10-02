import asyncio
import binascii

from ..utils import add_0x


class Web3Mixin:

    @asyncio.coroutine
    def web3_clientVersion(self):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#web3_clientversion

        :return: version
        :rtype: str
        """
        return (yield from self.rpc_call('web3_clientVersion'))

    @asyncio.coroutine
    def web3_sha3(self, data):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#web3_sha3

        :param data: Data for hashing
        :type data: str

        :return: Keccak-256
        :rtype: str
        """
        data = add_0x(binascii.hexlify(str(data).encode('utf-8')))
        return (yield from self.rpc_call('web3_sha3', [data]))
