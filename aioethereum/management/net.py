import asyncio

from ..utils import hex_to_dec


class NetMixin:

    @asyncio.coroutine
    def net_version(self):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#net_version

        :rtype: str
        """
        return (yield from self.rpc_call('net_version'))

    @asyncio.coroutine
    def net_listening(self):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#net_listening

        :rtype: bool
        """
        return (yield from self.rpc_call('net_listening'))

    @asyncio.coroutine
    def net_peerCount(self):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#net_peercount

        :rtype: int
        """
        return hex_to_dec((yield from self.rpc_call('net_peerCount')))
