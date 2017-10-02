from .constants import BLOCK_TAGS


def add_0x(string):
    if isinstance(string, bytes):
        string = string.decode('utf-8')
    return '0x' + str(string)


def hex_to_dec(x):
    return int(x, 16)


def ether_to_wei(ether):
    """Convert ether to wei
    """
    return int(ether * 10**18)


def validate_block(block):
    if isinstance(block, str):
        if block not in BLOCK_TAGS:
            raise ValueError('Invalid block tag.')
    elif isinstance(block, int):
        block = hex(block)
    else:
        raise ValueError('Invalid block type.')
    return block
