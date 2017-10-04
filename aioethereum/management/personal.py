import asyncio

from ..utils import ether_to_wei


class PersonalMixin:

    @asyncio.coroutine
    def personal_importRawKey(self, keydata, passphrase):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#personal_importrawkey

        :param keydata: Unencrypted private key
        :type keydata: str

        :param passphrase: Passphrase of private key
        :type passphrase: str

        :return: address
        :rtype: hex
        """
        return (yield from self.rpc_call('personal_importRawKey',
                                         [keydata, passphrase]))

    @asyncio.coroutine
    def personal_listAccounts(self):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#personal_listaccounts

        :return: addresses
        :rtype: list
        """
        return (yield from self.rpc_call('personal_listAccounts'))

    @asyncio.coroutine
    def personal_lockAccount(self, address):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#personal_lockaccount

        :param address: Account address
        :type address: str

        :rtype: bool
        """
        return (yield from self.rpc_call('personal_lockAccount', [address]))

    @asyncio.coroutine
    def personal_newAccount(self, passphrase=None):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#personal_newaccount

        :param passphrase: Passphrase of account (optional)
        :type passphrase: str

        :return: address
        :rtype: str
        """
        result = yield from self._call('personal_newAccount', [passphrase])
        return result

    @asyncio.coroutine
    def personal_unlockAccount(self, address, passphrase=None, duration=None):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#personal_unlockaccount

        :param address: Account address
        :type address: str

        :param passphrase: Passphrase of account (optional)
        :type passphrase: str

        :param duration: Duration to be unlocked (optional)
        :type duration: int

        :rtype: bool
        """
        result = yield from self._call('personal_unlockAccount',
                                       [address, passphrase, duration])
        return result

    @asyncio.coroutine
    def personal_sendTransaction(self, from_, to=None, gas=None,
                                 gas_price=None, value=None, data=None,
                                 nonce=None, passphrase=None):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#personal_sendtransaction

        :param from_: From account address
        :type from_: str

        :param to: To account address (optional)
        :type to: str

        :param gas: Gas amount for current transaction (optional)
        :type gas: int

        :param gas_price: Gas price for current transaction (optional)
        :type gas_price: int

        :param value: Amount of ether to send (optional)
        :type value: int

        :param data: Additional data for transaction (optional)
        :type data: hex

        :param nonce: Unique nonce for transaction (optional)
        :type nonce: int

        :param passphrase: Passphrase of account (optional)
        :type passphrase: str

        :return: txhash
        :rtype: str
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
            obj['value'] = hex(ether_to_wei(value))
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

        :param message: Message for sign
        :type message: str

        :param account: Account address
        :type account: str

        :param password: Password of account (optional)
        :type password: str

        :return: signature
        :rtype: str
        """
        result = yield from self._call('personal_sign',
                                       [message, account, password])
        return result

    @asyncio.coroutine
    def personal_ecRecover(self, message, signature):
        """https://github.com/ethereum/go-ethereum/wiki/Management-APIs#personal_ecrecover

        :param message: Message for sign
        :type message: str

        :param password: Signature of account (optional)
        :type password: str

        :return: address
        :rtype: str
        """
        result = yield from self._call('personal_ecRecover',
                                       [message, signature])
        return result
