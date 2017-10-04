import warnings
import asyncio

from ..utils import hex_to_dec, validate_block, ether_to_wei
from ..constants import BLOCK_TAG_LATEST


class EthMixin:

    @asyncio.coroutine
    def eth_protocolVersion(self):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_protocolversion

        :rtype: int
        """
        return hex_to_dec((yield from self.rpc_call('eth_protocolVersion')))

    @asyncio.coroutine
    def eth_syncing(self):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_syncing

        :return: sync status or false
        :rtype: dict or bool
        """
        return (yield from self.rpc_call('eth_syncing'))

    @asyncio.coroutine
    def eth_coinbase(self):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_coinbase

        :return: address
        :rtype: str
        """
        return (yield from self.rpc_call('eth_coinbase'))

    @asyncio.coroutine
    def eth_mining(self):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_mining

        :rtype: bool
        """
        return (yield from self.rpc_call('eth_mining'))

    @asyncio.coroutine
    def eth_hashrate(self):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_hashrate

        :return: hashrate
        :rtype: int
        """
        return hex_to_dec((yield from self.rpc_call('eth_hashrate')))

    @asyncio.coroutine
    def eth_gasPrice(self):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_gasprice

        :return: wei
        :rtype: int
        """
        return hex_to_dec((yield from self.rpc_call('eth_gasPrice')))

    @asyncio.coroutine
    def eth_accounts(self):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_accounts

        :return: accounts
        :rtype: list
        """
        return (yield from self.rpc_call('eth_accounts'))

    @asyncio.coroutine
    def eth_blockNumber(self):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_blocknumber

        :return: bnumber
        :rtype: int
        """
        return hex_to_dec((yield from self.rpc_call('eth_blockNumber')))

    @asyncio.coroutine
    def eth_getBalance(self, address, block=BLOCK_TAG_LATEST):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getbalance

        :param address: Account address
        :type address: str

        :param block: Block tag or number (optional)
        :type block: int or BLOCK_TAGS

        :return: wei
        :rtype: int
        """
        block = validate_block(block)
        return hex_to_dec((yield from self.rpc_call('eth_getBalance',
                                                    [address, block])))

    @asyncio.coroutine
    def eth_getStorageAt(self, address, position=0, block=BLOCK_TAG_LATEST):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getstorageat

        :param address: Storage address
        :type address: str

        :param position: Position in storage (optional)
        :type position: int

        :param block: Block tag or number (optional)
        :type block: int or BLOCK_TAGS

        :rtype: int
        """
        block = validate_block(block)
        return hex_to_dec((yield from self.rpc_call('eth_getStorageAt',
                                                    [address,
                                                     hex(position),
                                                     block])))

    @asyncio.coroutine
    def eth_getTransactionCount(self, address, block=BLOCK_TAG_LATEST):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_gettransactioncount

        :param address: Account address
        :type address: str

        :param block: Block tag or number (optional)
        :type block: int or BLOCK_TAGS

        :return: count
        :rtype: int
        """
        block = validate_block(block)
        return hex_to_dec((yield from self.rpc_call('eth_getTransactionCount',
                                                    [address, block])))

    @asyncio.coroutine
    def eth_getBlockTransactionCountByHash(self, bhash):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getblocktransactioncountbyhash

        :param bhash: Block hash
        :type bhash: str

        :return: count
        :rtype: int or None
        """
        response = yield from self.rpc_call('eth_getBlockTransactionCountByHash',
                                            [bhash])
        if response:
            return hex_to_dec(response)
        return response

    @asyncio.coroutine
    def eth_getBlockTransactionCountByNumber(self, block=BLOCK_TAG_LATEST):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getblocktransactioncountbynumber

        :param block: Block tag or number (optional)
        :type block: int or BLOCK_TAGS

        :return: count
        :rtype: int
        """
        block = validate_block(block)
        return hex_to_dec((yield from self.rpc_call('eth_getBlockTransactionCountByNumber',
                                                    [block])))

    @asyncio.coroutine
    def eth_getUncleCountByBlockHash(self, bhash):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getunclecountbyblockhash

        :param bhash: Block hash
        :type bhash: str

        :return: count
        :rtype: int or None
        """
        response = yield from self.rpc_call('eth_getUncleCountByBlockHash',
                                            [bhash])
        if response:
            return hex_to_dec(response)
        return response

    @asyncio.coroutine
    def eth_getUncleCountByBlockNumber(self, block=BLOCK_TAG_LATEST):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getunclecountbyblocknumber

        :param block: Block tag or number (optional)
        :type block: int or BLOCK_TAGS

        :return: count
        :rtype: int
        """
        block = validate_block(block)
        response = yield from self.rpc_call('eth_getUncleCountByBlockNumber',
                                            [block])
        if response:
            return hex_to_dec(response)
        return response

    @asyncio.coroutine
    def eth_getCode(self, address, block=BLOCK_TAG_LATEST):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getcode

        :param address: Address of contract
        :type address: str

        :param block: Block tag or number (optional)
        :type block: int or BLOCK_TAGS

        :return: code
        :rtype: str
        """
        block = validate_block(block)
        return (yield from self.rpc_call('eth_getCode', [address, block]))

    @asyncio.coroutine
    def eth_sign(self, address, data):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_sign

        :param address: Account address
        :type address: str

        :param data: Message to sign
        :type data: str

        :return: signature
        :rtype: str
        """
        return (yield from self.rpc_call('eth_sign', [address, data]))

    @asyncio.coroutine
    def eth_sendTransaction(self, from_, to=None, gas=None,
                            gas_price=None, value=None, data=None,
                            nonce=None):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_sendtransaction

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

        return (yield from self.rpc_call('eth_sendTransaction', [obj]))

    @asyncio.coroutine
    def eth_sendRawTransaction(self, data):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_sendrawtransaction

        :param data: Signed transaction data
        :type data: str

        :return: txhash
        :rtype: str
        """
        return (yield from self.rpc_call('eth_sendRawTransaction', [data]))

    @asyncio.coroutine
    def eth_call(self, from_, to=None, gas=None,
                 gas_price=None, value=None, data=None,
                 block=BLOCK_TAG_LATEST):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_call

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

        :param block: Block tag or number (optional)
        :type block: int or BLOCK_TAGS

        :rtype: str
        """
        block = validate_block(block)
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

        return (yield from self.rpc_call('eth_call', [obj, block]))

    @asyncio.coroutine
    def eth_estimateGas(self, from_, to=None, gas=None,
                        gas_price=None, value=None, data=None):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_estimategas

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

        :return: gas amount
        :rtype: int
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

        return hex_to_dec((yield from self.rpc_call('eth_estimateGas', [obj])))

    @asyncio.coroutine
    def eth_getBlockByHash(self, bhash, tx_objects=True):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getblockbyhash

        :param bhash: Block hash
        :type bhash: str

        :param tx_objects: Return txs full object (optional)
        :type tx_objects: bool

        :return: block
        :rtype: dict or None
        """
        result = yield from self.rpc_call('eth_getBlockByHash',
                                          [bhash, tx_objects])
        # TODO: Update result response
        return result

    @asyncio.coroutine
    def eth_getBlockByNumber(self, block=BLOCK_TAG_LATEST, tx_objects=True):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getblockbynumber

        :param block: Block tag or number (optional)
        :type block: int or BLOCK_TAGS

        :param tx_objects: Return txs full object (optional)
        :type tx_objects: bool

        :return: block
        :rtype: dict or None
        """
        block = validate_block(block)
        result = yield from self.rpc_call('eth_getBlockByNumber',
                                          [block, tx_objects])
        # TODO: Update result response
        return result

    @asyncio.coroutine
    def eth_getTransactionByHash(self, txhash):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_gettransactionbyhash

        :param txhash: Transaction hash
        :type txhash: str

        :return: transaction
        :rtype: dict or None
        """
        result = yield from self.rpc_call('eth_getTransactionByHash', [txhash])
        # TODO: Update result response
        return result

    @asyncio.coroutine
    def eth_getTransactionByBlockHashAndIndex(self, bhash, index=0):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_gettransactionbyblockhashandindex

        :param bhash: Block hash
        :type bhash: str

        :param index: Index position (optional)
        :type index: int
        """
        result = yield from self.rpc_call('eth_getTransactionByBlockHashAndIndex',
                                          [bhash, hex(index)])
        # TODO: Update result response
        return result

    @asyncio.coroutine
    def eth_getTransactionByBlockNumberAndIndex(self, block=BLOCK_TAG_LATEST,
                                                index=0):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_gettransactionbyblocknumberandindex

        :param block: Block tag or number (optional)
        :type block: int or BLOCK_TAGS

        :param index: Index position (optional)
        :type index: int

        :return: transaction
        :rtype: dict or None
        """
        block = validate_block(block)
        result = yield from self.rpc_call('eth_getTransactionByBlockNumberAndIndex',
                                          [block, hex(index)])
        # TODO: Update result response
        return result

    @asyncio.coroutine
    def eth_getTransactionReceipt(self, txhash):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_gettransactionreceipt

        :param txhash: Transaction hash
        :type txhash: str

        :return: transaction
        :rtype: dict or None
        """
        result = yield from self.rpc_call('eth_getTransactionReceipt',
                                          [txhash])
        # TODO: Update result response
        return result

    @asyncio.coroutine
    def eth_getUncleByBlockHashAndIndex(self, bhash, index=0):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getunclebyblockhashandindex

        :param bhash: Block hash
        :type bhash: str

        :param index: Index position (optional)
        :type index: int

        :return: block
        :rtype: dict or None
        """
        result = yield from self.rpc_call('eth_getUncleByBlockHashAndIndex',
                                          [bhash, hex(index)])
        # TODO: Update result response
        return result

    @asyncio.coroutine
    def eth_getUncleByBlockNumberAndIndex(self, block=BLOCK_TAG_LATEST,
                                          index=0):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getunclebyblocknumberandindex

        :param block: Block tag or number (optional)
        :type block: int or BLOCK_TAGS

        :param index: Index position (optional)
        :type index: int

        :return: block
        :rtype: dict or None
        """
        block = validate_block(block)
        result = yield from self.rpc_call('eth_getUncleByBlockNumberAndIndex',
                                          [block, hex(index)])
        # TODO: Update result response
        return result

    @asyncio.coroutine
    def eth_getCompilers(self):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getcompilers

        DEPRECATED
        """
        warnings.warn('deprecated', DeprecationWarning)
        return (yield from self.rpc_call('eth_getCompilers'))

    @asyncio.coroutine
    def eth_compileSolidity(self, code):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_compilesolidity

        DEPRECATED
        """
        warnings.warn('deprecated', DeprecationWarning)
        return (yield from self.rpc_call('eth_compileSolidity', [code]))

    @asyncio.coroutine
    def eth_compileLLL(self, code):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_compilelll

        DEPRECATED
        """
        warnings.warn('deprecated', DeprecationWarning)
        return (yield from self.rpc_call('eth_compileLLL', [code]))

    @asyncio.coroutine
    def eth_compileSerpent(self, code):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_compileserpent

        DEPRECATED
        """
        warnings.warn('deprecated', DeprecationWarning)
        return (yield from self.rpc_call('eth_compileSerpent', [code]))

    @asyncio.coroutine
    def eth_newFilter(self, from_block=BLOCK_TAG_LATEST,
                      to_block=BLOCK_TAG_LATEST, address=None, topics=None):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_newfilter

        :param from_block: Block tag or number (optional)
        :type from_block: int or BLOCK_TAGS

        :param to_block: Block tag or number (optional)
        :type to_block: int or BLOCK_TAGS

        :param address: Contract address (optional)
        :type address: str

        :param topics: Topics (optional)
        :type topics: list

        :return: filter_id
        :rtype: str
        """
        obj = {
            'fromBlock': validate_block(from_block),
            'toBlock': validate_block(to_block),
            'address': address,
            'topics': topics
        }
        return (yield from self.rpc_call('eth_newFilter', [obj]))

    @asyncio.coroutine
    def eth_newBlockFilter(self):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_newblockfilter

        :return: filter_id
        :rtype: str
        """
        return (yield from self.rpc_call('eth_newBlockFilter'))

    @asyncio.coroutine
    def eth_newPendingTransactionFilter(self):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_newpendingtransactionfilter

        :return: filter_id
        :rtype: str
        """
        return (yield from self.rpc_call('eth_newPendingTransactionFilter'))

    @asyncio.coroutine
    def eth_uninstallFilter(self, filter_id):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_uninstallfilter

        :param filter_id: Id of created filter
        :type filter_id: str

        :return: success
        :rtype: bool
        """
        return (yield from self.rpc_call('eth_uninstallFilter', [filter_id]))

    @asyncio.coroutine
    def eth_getFilterChanges(self, filter_id):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getfilterchanges

        :param filter_id: Id of created filter
        :type filter_id: str

        :return: logs
        :rtype: list
        """
        return (yield from self.rpc_call('eth_getFilterChanges', [filter_id]))

    @asyncio.coroutine
    def eth_getFilterLogs(self, filter_id):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getfilterlogs

        :param filter_id: Id of created filter
        :type filter_id: str

        :return: logs
        :rtype: list
        """
        return (yield from self.rpc_call('eth_getFilterLogs', [filter_id]))

    @asyncio.coroutine
    def eth_getLogs(self, from_block=BLOCK_TAG_LATEST,
                    to_block=BLOCK_TAG_LATEST, address=None, topics=None):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getlogs

        :param from_block: Block tag or number (optional)
        :type from_block: int or BLOCK_TAGS

        :param to_block: Block tag or number (optional)
        :type to_block: int or BLOCK_TAGS

        :param address: Contract address (optional)
        :type address: str

        :param topics: Topics (optional)
        :type topics: list

        :return: logs
        :rtype: list
        """
        obj = {
            'fromBlock': validate_block(from_block),
            'toBlock': validate_block(to_block),
            'address': address,
            'topics': topics
        }
        result = yield from self.rpc_call('eth_getLogs', [obj])
        return result

    @asyncio.coroutine
    def eth_getWork(self):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getwork

        :return: work
        :rtype: list
        """
        return (yield from self.rpc_call('eth_getWork'))

    @asyncio.coroutine
    def eth_submitWork(self, nonce, header, mix_digest):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_submitwork

        :param nonce: Nonce of work
        :type nonce: int

        :param header: Pow-hash header
        :type header: str

        :param mix_digest: Mix digest
        :type mix_digest: str

        :return: success
        :rtype: bool
        """
        return (yield from self.rpc_call('eth_submitWork',
                                         [nonce, header, mix_digest]))

    @asyncio.coroutine
    def eth_submitHashrate(self, hashrate, id_):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_submithashrate

        :param hashrate: Hash rate
        :type hashrate: str

        :param id_: Random hex
        :type id_: str

        :return: success
        :rtype: bool
        """
        return (yield from self.rpc_call('eth_submitHashrate',
                                         [hex(hashrate), id_]))
