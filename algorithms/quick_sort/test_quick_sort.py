import pytest
from quick_sort import *
import random


def test_simple():
    array = [2, 3, 1, 5, 4]
    quick_sort_array(array)
    assert array == [1, 2, 3, 4, 5]


def test_sorted_already():
    array = [1, 2, 3, 4, 5]
    quick_sort_array(array)
    assert array == [1, 2, 3, 4, 5]


def test_sorted_indir():
    array = [5, 4, 3, 2, 1]
    quick_sort_array(array)
    assert array == [1, 2, 3, 4, 5]

def test_many_same_items():
    array = [3, 7, 8, 3, 3, 1, 4, 3, 1]
    quick_sort_array(array)
    assert array == [1, 1, 3, 3, 3, 3, 4, 7, 8]


def test_empty():
    array = []
    quick_sort_array(array)
    assert array == []


def test_one_element():
    array = [1]
    quick_sort_array(array)
    assert array == [1]


def test_big_random_array():
    array = [random.randint(1, 1000) for _ in range(1000)]
    print(array)
    sorted_array = sorted(array)    # system sort for checking
    quick_sort_array(array)
    print(array)
    assert array == sorted_array


