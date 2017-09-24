from .admin import AdminMixin
from .db import DbMixin
from .debug import DebugMixin
from .eth import EthMixin
from .miner import MinerMixin
from .net import NetMixin
from .personal import PersonalMixin
from .shh import ShhMixin
from .txpool import TxpoolMixin
from .web3 import Web3Mixin


__all__ = [
    'AdminMixin',
    'DbMixin',
    'DebugMixin',
    'EthMixin',
    'MinerMixin',
    'NetMixin',
    'PersonalMixin',
    'ShhMixin',
    'TxpoolMixin',
    'Web3Mixin',
    'RpcMixin',
]


class RpcMixin(AdminMixin, DbMixin, DebugMixin, EthMixin, MinerMixin,
               NetMixin, PersonalMixin, ShhMixin, TxpoolMixin, Web3Mixin):
    pass
