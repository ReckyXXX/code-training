import pytest
from median_out_of_three import *


# task tests:

def test1():
    assert median_out_of_three([1, 2, 3]) == 2


def test2():
    assert median_out_of_three([1000, -1000, 0]) == 0


def test3():
    assert median_out_of_three([3, 1, 3]) == 3

# my tests:

def test_already_sorted():
    assert median_out_of_three([1, 2, 3]) == 2


def test_non_sorted_first():
    assert median_out_of_three([2, 1, 3]) == 2


def test_non_sorted_last():
    assert median_out_of_three([1, 3, 2]) == 2
    

def test_equal_part():
    assert median_out_of_three([1, 50, 1]) == 1


def test_equal_all():
    assert median_out_of_three([1, 1, 1]) == 1


def test_negative_one():
    assert median_out_of_three([-100, 100, 0]) == 0


def test_negative_all():
    assert median_out_of_three([-100, -105, -10]) == -100


def test_bounds():
    assert median_out_of_three([-1000, 1000, 0]) == 0

