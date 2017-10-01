.. aioethereum documentation master file, created by
   sphinx-quickstart on Sun Oct  1 13:37:24 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

aioethereum
===========

Ethereum RPC client library for the (:pep:`3156`) Python event loop.

The library is intended to provide simple and clear interface to Ethereum node
based on :term:`asyncio`.


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


Installation
------------

The easiest way to install aioethereum is by using the package on PyPi::

   pip install aioethereum


Requirements
------------

- Python 3.3 and :term:`asyncio` or Python 3.4+
- :term:`ujson`


License
-------

The aioethereum is offered under MIT license.

----

Getting started
---------------

.. toctree::
   :maxdepth: 2

   start

API Documentation
-----------------

.. toctree::
   :maxdepth: 4

   base


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _MIT license: https://github.com/DeV1doR/aioethereum/blob/master/LICENSE.md
