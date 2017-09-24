import asyncio


class PersonalMixin:

    @asyncio.coroutine
    def personal_importRawKey(self, keydata, passphrase):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#personal_importrawkey
        """
        result = yield from self._call('personal_importRawKey',
                                       [keydata, passphrase])
        return result

    @asyncio.coroutine
    def personal_listAccounts(self):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#personal_listaccounts
        """
        result = yield from self._call('personal_listAccounts')
        return result

    @asyncio.coroutine
    def personal_lockAccount(self, address):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#personal_lockaccount
        """
        result = yield from self._call('personal_lockAccount', [address])
        return result

    @asyncio.coroutine
    def personal_newAccount(self, passphrase=None):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#personal_newaccount
        """
        result = yield from self._call('personal_newAccount', [passphrase])
        return result

    @asyncio.coroutine
    def personal_unlockAccount(self, address, passphrase, duration=None):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#personal_unlockaccount
        """
        result = yield from self._call('personal_unlockAccount',
                                       [address, passphrase, duration])
        return result

    @asyncio.coroutine
    def personal_sendTransaction(self, from_, to=None, gas=None,
                                 gas_price=None, value=None, data=None,
                                 nonce=None, passphrase=None):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#personal_sendtransaction
        """
        obj = {}
        obj['from'] = from_
        if to is not None:
            obj['to'] = to
        if gas is not None:
            obj['gas'] = hex(gas)
        if gas_price is not None:
            obj['gasPrice'] = hex(gas_price)
        if value is not None:
            obj['value'] = hex(value)
        if data is not None:
            obj['data'] = data
        if nonce is not None:
            obj['nonce'] = hex(nonce)

        result = yield from self._call('personal_sendTransaction',
                                       [obj, passphrase])
        return result

    @asyncio.coroutine
    def personal_sign(self, message, account, password=None):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#personal_sign
        """
        result = yield from self._call('personal_sign',
                                       [message, account, password])
        return result

    @asyncio.coroutine
    def personal_ecRecover(self, message, signature):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#personal_ecrecover
        """
        result = yield from self._call('personal_ecRecover',
                                       [message, signature])
        return result
