import warnings
import asyncio

from ..utils import hex_to_dec, validate_block
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
        response = yield from self._call('eth_getUncleCountByBlockHash',
                                         [bhash])
        if response:
            return hex_to_dec(response)
        return response

    @asyncio.coroutine
    def eth_getUncleCountByBlockNumber(self, block=BLOCK_TAG_LATEST):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getunclecountbyblocknumber
        """
        block = validate_block(block)
        result = yield from self._call('eth_getUncleCountByBlockNumber',
                                       [block])
        return hex_to_dec(result)

    @asyncio.coroutine
    def eth_getCode(self, address, block=BLOCK_TAG_LATEST):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getcode
        """
        block = validate_block(block)
        result = yield from self._call('eth_getCode', [address, block])
        return result

    @asyncio.coroutine
    def eth_sign(self, address, data):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_sign
        """
        result = yield from self._call('eth_sign', [address, hex(data)])
        return result

    @asyncio.coroutine
    def eth_sendTransaction(self, from_, to=None, gas=None,
                            gas_price=None, value=None, data=None,
                            nonce=None):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_sendtransaction
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

        result = yield from self._call('eth_sendTransaction', [obj])
        return result

    @asyncio.coroutine
    def eth_sendRawTransaction(self, data):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_sendrawtransaction
        """
        result = yield from self._call('eth_sendRawTransaction', [data])
        return result

    @asyncio.coroutine
    def eth_call(self, from_, to=None, gas=None,
                 gas_price=None, value=None, data=None,
                 block=BLOCK_TAG_LATEST):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_call
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
            obj['value'] = hex(value)
        if data is not None:
            obj['data'] = data

        result = yield from self._call('eth_call', [obj, block])
        return result

    @asyncio.coroutine
    def eth_estimateGas(self, from_, to=None, gas=None,
                        gas_price=None, value=None, data=None):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_estimategas
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

        result = yield from self._call('eth_estimateGas', [obj])
        return hex_to_dec(result)

    @asyncio.coroutine
    def eth_getBlockByHash(self, bhash, tx_objects=True):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getblockbyhash
        """
        result = yield from self._call('eth_getBlockByHash',
                                       [bhash, tx_objects])
        # TODO: Update result response
        return result

    @asyncio.coroutine
    def eth_getBlockByNumber(self, block=BLOCK_TAG_LATEST, tx_objects=True):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getblockbynumber
        """
        block = validate_block(block)
        result = yield from self._call('eth_getBlockByNumber',
                                       [block, tx_objects])
        # TODO: Update result response
        return result

    @asyncio.coroutine
    def eth_getTransactionByHash(self, txhash):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_gettransactionbyhash
        """
        result = yield from self._call('eth_getTransactionByHash', [txhash])
        # TODO: Update result response
        return result

    @asyncio.coroutine
    def eth_getTransactionByBlockHashAndIndex(self, bhash, index=0):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_gettransactionbyblockhashandindex
        """
        result = yield from self._call('eth_getTransactionByBlockHashAndIndex',
                                       [bhash, hex(index)])
        # TODO: Update result response
        return result

    @asyncio.coroutine
    def eth_getTransactionByBlockNumberAndIndex(self, block=BLOCK_TAG_LATEST,
                                                index=0):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_gettransactionbyblocknumberandindex
        """
        block = validate_block(block)
        result = yield from self._call('eth_getTransactionByBlockNumberAndIndex',
                                       [block, hex(index)])
        return result

    @asyncio.coroutine
    def eth_getTransactionReceipt(self, txhash):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_gettransactionreceipt
        """
        result = yield from self._call('eth_getTransactionReceipt', [txhash])
        # TODO: Update result response
        return result

    @asyncio.coroutine
    def eth_getUncleByBlockHashAndIndex(self, bhash, index=0):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getunclebyblockhashandindex
        """
        result = yield from self._call('eth_getUncleByBlockHashAndIndex',
                                       [bhash, hex(index)])
        # TODO: Update result response
        return result

    @asyncio.coroutine
    def eth_getUncleByBlockNumberAndIndex(self, block=BLOCK_TAG_LATEST,
                                          index=0):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getunclebyblocknumberandindex
        """
        block = validate_block(block)
        result = yield from self._call('eth_getUncleByBlockNumberAndIndex',
                                       [block, hex(index)])
        # TODO: Update result response
        return result

    @asyncio.coroutine
    def eth_getCompilers(self):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getcompilers
        DEPRECATED
        """
        warnings.warn('deprecated', DeprecationWarning)
        result = yield from self._call('eth_getCompilers')
        return result

    @asyncio.coroutine
    def eth_compileSolidity(self, code):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_compilesolidity
        DEPRECATED
        """
        warnings.warn('deprecated', DeprecationWarning)
        result = yield from self._call('eth_compileSolidity', [code])
        return result

    @asyncio.coroutine
    def eth_compileLLL(self, code):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_compilelll
        DEPRECATED
        """
        warnings.warn('deprecated', DeprecationWarning)
        result = yield from self._call('eth_compileLLL', [code])
        return result

    @asyncio.coroutine
    def eth_compileSerpent(self, code):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_compileserpent
        DEPRECATED
        """
        warnings.warn('deprecated', DeprecationWarning)
        result = yield from self._call('eth_compileSerpent', [code])
        return result

    @asyncio.coroutine
    def eth_newFilter(self, from_block=BLOCK_TAG_LATEST,
                      to_block=BLOCK_TAG_LATEST, address=None, topics=None):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_newfilter
        """
        obj = {
            'fromBlock': validate_block(from_block),
            'toBlock': validate_block(to_block),
        }
        if address:
            obj['address'] = address
        if topics:
            obj['topics'] = topics

        result = yield from self._call('eth_newFilter', [obj])
        return result

    @asyncio.coroutine
    def eth_newBlockFilter(self):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_newblockfilter
        """
        result = yield from self._call('eth_newBlockFilter')
        return result

    @asyncio.coroutine
    def eth_newPendingTransactionFilter(self):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_newpendingtransactionfilter
        """
        result = yield from self._call('eth_newPendingTransactionFilter')
        return result

    @asyncio.coroutine
    def eth_uninstallFilter(self, filter_id):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_uninstallfilter
        """
        result = yield from self._call('eth_uninstallFilter', [filter_id])
        return result

    @asyncio.coroutine
    def eth_getFilterChanges(self, filter_id):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getfilterchanges
        """
        result = yield from self._call('eth_getFilterChanges', [filter_id])
        return result

    @asyncio.coroutine
    def eth_getFilterLogs(self, filter_id):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getfilterlogs
        """
        result = yield from self._call('eth_getFilterLogs', [filter_id])
        return result

    @asyncio.coroutine
    def eth_getLogs(self, from_block=BLOCK_TAG_LATEST,
                    to_block=BLOCK_TAG_LATEST, address=None, topics=None):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getlogs
        """
        obj = {
            'fromBlock': validate_block(from_block),
            'toBlock': validate_block(to_block),
        }
        if address:
            obj['address'] = address
        if topics:
            obj['topics'] = topics
        result = yield from self._call('eth_getLogs', [obj])
        return result

    @asyncio.coroutine
    def eth_getWork(self):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getwork
        """
        result = yield from self._call('eth_getWork')
        return result

    @asyncio.coroutine
    def eth_submitWork(self, nonce, header, mix_digest):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_submitwork
        """
        result = yield from self._call('eth_submitWork',
                                       [nonce, header, mix_digest])
        return result

    @asyncio.coroutine
    def eth_submitHashrate(self, hashrate, id_):
        """https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_submithashrate
        """
        result = yield from self._call('eth_submitHashrate',
                                       [hex(hashrate), id_])
        return result
