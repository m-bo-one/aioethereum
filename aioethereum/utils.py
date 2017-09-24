from .constants import BLOCK_TAGS


def str_to_hex(string):
    return '0x' + str(string)


def hex_to_dec(x):
    return int(x, 16)


def validate_block(block):
    if isinstance(block, str):
        if block not in BLOCK_TAGS:
            raise ValueError('Invalid block tag.')
    elif isinstance(block, int):
        block = hex(block)
    else:
        raise ValueError('Invalid block type.')
    return block
