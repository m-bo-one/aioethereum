import warnings
import asyncio


class ShhMixin:

    @asyncio.coroutine
    def shh_version(self):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#shh_version

        :rtype: float
        """
        return float((yield from self.rpc_call('shh_version')))

    @asyncio.coroutine
    def shh_post(self, from_=None, to=None, *, topics, payload, priority, ttl):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#shh_post
        """
        # FIXME: Not working
        obj = {
            'from': from_,
            'to': to,
            'topics': topics,
            'payload': payload,
            'priority': hex(priority),
            'ttl': hex(ttl),
        }
        return float((yield from self.rpc_call('shh_post', [obj])))

    @asyncio.coroutine
    def shh_newIdentity(self):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#shh_newidentity

        DEPRECATED
        """
        warnings.warn('deprecated', DeprecationWarning)
        return (yield from self.rpc_call('shh_newIdentity'))

    @asyncio.coroutine
    def shh_hasIdentity(self, address):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#shh_hasidentity

        DEPRECATED
        """
        warnings.warn('deprecated', DeprecationWarning)
        return (yield from self.rpc_call('shh_hasIdentity', [address]))

    @asyncio.coroutine
    def shh_newGroup(self):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#shh_newgroup

        DEPRECATED
        """
        warnings.warn('deprecated', DeprecationWarning)
        result = yield from self.rpc_call('shh_newGroup')
        return result

    @asyncio.coroutine
    def shh_addToGroup(self):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#shh_addtogroup

        DEPRECATED
        """
        warnings.warn('deprecated', DeprecationWarning)
        return (yield from self.rpc_call('shh_addToGroup'))

    @asyncio.coroutine
    def shh_newFilter(self, to=None, *, topics):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#shh_newfilter

        DEPRECATED
        """
        obj = {
            'to': to,
            'topics': topics,
        }
        warnings.warn('deprecated', DeprecationWarning)
        return (yield from self.rpc_call('shh_newFilter', [obj]))

    @asyncio.coroutine
    def shh_uninstallFilter(self, filter_id):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#shh_uninstallfilter

        DEPRECATED
        """
        warnings.warn('deprecated', DeprecationWarning)
        return (yield from self.rpc_call('shh_uninstallFilter', [filter_id]))

    @asyncio.coroutine
    def shh_getFilterChanges(self, filter_id):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#shh_getfilterchanges

        DEPRECATED
        """
        warnings.warn('deprecated', DeprecationWarning)
        return (yield from self.rpc_call('shh_getFilterChanges', [filter_id]))

    @asyncio.coroutine
    def shh_getMessages(self, filter_id):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#shh_getmessages

        DEPRECATED
        """
        warnings.warn('deprecated', DeprecationWarning)
        return (yield from self.rpc_call('shh_getMessages', [filter_id]))
