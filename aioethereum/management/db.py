import warnings
import asyncio

from ..utils import add_0x


class DbMixin:

    @asyncio.coroutine
    def db_putString(self, db_name, key, value):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#db_putstring

        DEPRECATED
        """
        warnings.warn('deprecated', DeprecationWarning)
        result = yield from self._call('db_putString', [db_name, key, value])
        return result

    @asyncio.coroutine
    def db_getString(self, db_name, key):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#db_getstring

        DEPRECATED
        """
        warnings.warn('deprecated', DeprecationWarning)
        result = yield from self._call('db_getString', [db_name, key])
        return result

    @asyncio.coroutine
    def db_putHex(self, db_name, key, value):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#db_puthex

        DEPRECATED
        """
        warnings.warn('deprecated', DeprecationWarning)
        if not value.startswith('0x'):
            value = add_0x(value)
        result = yield from self._call('db_putHex', [db_name, key, value])
        return result

    def db_getHex(self, db_name, key):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#db_gethex

        DEPRECATED
        """
        warnings.warn('deprecated', DeprecationWarning)
        result = yield from self._call('db_getHex', [db_name, key])
        return result
