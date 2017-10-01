|pypi| |license| |docs|

aioethereum
===========

Ethereum RPC client library for the `PEP 3156`_ Python event loop.

.. _PEP 3156: http://legacy.python.org/dev/peps/pep-3156/

Features
--------

================================  ==============================
ujson_ support                      Yes
High-level APIs                     Yes
HTTP support                        Yes
Unix domain socket (IPC) support    Yes
SSL/TLS support                     Yes
Tested CPython versions             `3.4, 3.5, 3.6`
Tested for Geth node                `1.7.0`
Implemented RPC apis                `db, eth, miner, net, personal, shh, txpool, web3`
================================  ==============================

Documentation
-------------

TODO

Usage examples
--------------

Simple high-level interface (through HTTP):

.. code:: python

    import asyncio
    import aioethereum

    loop = asyncio.get_event_loop()

    async def go():
        client = await aioethereum.create_ethereum_client(
            'http://localhost:8545', loop=loop)
        val = await client.web3_clientVersion()
        print(val)

    loop.run_until_complete(go())
    # will print like 'Geth/v1.7.0-stable-6c6c7b2a/darwin-amd64/go1.9'


or via IPC

.. code:: python

    import asyncio
    import aioethereum

    loop = asyncio.get_event_loop()

    async def go():
        client = await aioethereum.create_ethereum_client(
            'ipc://<path_to_unix_socket>', loop=loop)
        val = await client.web3_clientVersion()
        print(val)

    loop.run_until_complete(go())
    # will print like 'Geth/v1.7.0-stable-6c6c7b2a/darwin-amd64/go1.9'


Requirements
------------

* Python_ 3.3+
* asyncio_ or Python_ 3.4+
* ujson_
* aiohttp_

.. note::

    ujson is preferred requirement.
    Pure C JSON encoder and decoder is implemented as well and can be used
    automatically when installed.


License
-------

The aioethereum is offered under MIT license.

.. _Python: https://www.python.org
.. _asyncio: https://pypi.python.org/pypi/asyncio
.. _aiohttp: https://pypi.python.org/pypi/aiohttp
.. _ujson: https://pypi.python.org/pypi/ujson


TODO
----

* Add tests for all management RPC apis
* Add admin and debug apis
* Add sphinx docs


.. |pypi| image:: https://img.shields.io/pypi/v/aioethereum.svg?style=flat&label=latest%20version
    :target: https://pypi.python.org/pypi/aioethereum
    :alt: Latest version released on PyPi

.. |license| image:: https://img.shields.io/pypi/l/aioethereum.svg?style=flat&label=license
    :target: https://github.com/DeV1doR/aioethereum/blob/master/LICENSE.md
    :alt: MIT License

.. |docs| image:: https://readthedocs.org/projects/aioethereum/badge/?version=latest
    :target: http://aioethereum.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation status
