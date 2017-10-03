from .constants import BLOCK_TAGS


def add_0x(string):
    """Add 0x to string at start.
    """
    if isinstance(string, bytes):
        string = string.decode('utf-8')
    return '0x' + str(string)


def hex_to_dec(x):
    """Convert hex to decimal
    """
    return int(x, 16)


def wei_to_ether(wei):
    """Convert wei to ether
    """
    return 1.0 * wei / 10**18


def gwei_to_ether(wei):
    """Convert gwei to ether
    """
    return 1.0 * wei / 10**9


def ether_to_wei(ether):
    """Convert ether to wei
    """
    return int(ether * 10**18)


def ether_to_gwei(ether):
    """Convert ether to Gwei
    """
    return int(ether * 10**9)


def validate_block(block):
    """Validate block on tag or hex int
    """
    if isinstance(block, str):
        if block not in BLOCK_TAGS:
            raise ValueError('Invalid block tag.')
    elif isinstance(block, int):
        block = hex(block)
    else:
        raise ValueError('Invalid block type.')
    return block
