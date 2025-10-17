import pytest
from coderun.knight_move.knight_move import *


# task tests:

def test1():
    assert calculate_knight_moves_count(3, 2) == 1


def test2():
    assert calculate_knight_moves_count(31, 34) == 293930

# my tests:

def test_common():
    assert calculate_knight_moves_count(2, 3) == 1


def test_no_moves():
    assert calculate_knight_moves_count(1, 3) == 0


def test_already_here():
    assert calculate_knight_moves_count(1, 1) == 1

@pytest.mark.timeout(1)
def test_max():
    assert calculate_knight_moves_count(50, 50) == 0

