import pytest

from aioethereum.constants import (
    BLOCK_TAG_EARLIEST, BLOCK_TAG_LATEST, BLOCK_TAG_PENDING)
from aioethereum.utils import (
    add_0x, hex_to_dec, validate_block,
    wei_to_ether, ether_to_wei, gwei_to_ether, ether_to_gwei)


def test_add_0x():
    result = add_0x(b'hello')
    assert '0xhello' == result

    result = add_0x('hello')
    assert '0xhello' == result

    result = add_0x(123)
    assert '0x123' == result


def test_hex_to_dec():
    result = hex_to_dec('-0x8')  # -8
    assert result == -8
    result = hex_to_dec('0x0')  # 0
    assert result == 0
    result = hex_to_dec('0x10')  # 16
    assert result == 16


def test_validate_block():
    result = validate_block(BLOCK_TAG_EARLIEST)
    assert result == BLOCK_TAG_EARLIEST

    result = validate_block(BLOCK_TAG_LATEST)
    assert result == BLOCK_TAG_LATEST

    result = validate_block(BLOCK_TAG_PENDING)
    assert result == BLOCK_TAG_PENDING

    result = validate_block(123)
    assert hex(123) == result

    # test invalid type
    with pytest.raises(ValueError) as excinfo:
        validate_block(123.34)
    assert 'type' in str(excinfo)

    # invalid tag
    with pytest.raises(ValueError) as excinfo:
        validate_block('incorrect')
    assert 'tag' in str(excinfo)


def test_wei_to_ether():
    """Test convertion wei to ether (it is 10 in -18 step).
    """
    result = wei_to_ether(10 ** 18)
    assert result == 1  # 1 ether
    result = wei_to_ether(1)
    assert result == 10 ** -18  # 1 in -18 step ether


def test_gwei_to_ether():
    """Test convertion gwei to ether (it is 10 in -9 step).
    """
    result = gwei_to_ether(10 ** 9)
    assert result == 1  # 1 ether
    result = gwei_to_ether(1)
    assert result == 10 ** -9  # 1 in -18 step ether


def test_ether_to_wei():
    """Test convertion ether to wei (it is 10 in 18 step).
    """
    result = ether_to_wei(1)
    assert result == 10 ** 18  # 10 in 18 step wei
    result = ether_to_wei(10 ** -18)
    assert result == 1  # 1 wei


def test_ether_to_gwei():
    """Test convertion ether to gwei (it is 10 in 9 step).
    """
    result = ether_to_gwei(1)
    assert result == 10 ** 9  # 10 in 9 step Gwei
    result = ether_to_gwei(10 ** -9)
    assert result == 1  # 1 Gwei
