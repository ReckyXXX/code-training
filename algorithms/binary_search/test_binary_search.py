import pytest
from binary_search import *


def test_simple():
    array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    index = binary_search(array, 70)
    assert index == 6

def test_first_element():
    array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    index = binary_search(array, 10)
    assert index == 0

def test_last_element():
    array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    index = binary_search(array, 100)
    assert index == 9

def test_equal():
    array = [10, 20, 30, 30, 30, 60, 70, 90, 90, 100]
    index = binary_search(array, 90)
    assert index == 7

def test_empty():
    array = []
    index = binary_search(array, 70)
    assert index == -1

def test_one_element():
    array = [10]
    index = binary_search(array, 10)
    assert index == 0