import asyncio

from ..utils import hex_to_dec


class NetMixin:

    @asyncio.coroutine
    def net_version(self):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#net_version
        """
        result = yield from self._call('net_version')
        return result

    @asyncio.coroutine
    def net_listening(self):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#net_listening
        """
        result = yield from self._call('net_listening')
        return result

    @asyncio.coroutine
    def net_peerCount(self):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#net_peercount
        """
        result = yield from self._call('net_peerCount')
        return hex_to_dec(result)
