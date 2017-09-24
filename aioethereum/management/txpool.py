import asyncio

from ..utils import hex_to_dec


class TxpoolMixin:

    @asyncio.coroutine
    def txpool_content(self):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#txpool_content
        """
        result = yield from self._call('txpool_content')
        # TODO: Update result response
        return result

    @asyncio.coroutine
    def txpool_inspect(self):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#txpool_inspect
        """
        result = yield from self._call('txpool_inspect')
        # TODO: Update result response
        return result

    @asyncio.coroutine
    def txpool_status(self):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#txpool_status
        """
        result = yield from self._call('txpool_status')
        return {k: hex_to_dec(v) for k, v in result.items()}
