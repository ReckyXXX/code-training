"""
    Difficulty: [Medium]
    Tags: sort

    Quicksort algorithm realization
    Speed: 
        mid: O(nlog(n))
        bad: O(n^2)
    Memory:
        all: O(log(n))
"""

import sys

def quick_sort_array(array):
    if (len(array) is 0):
        return
    quick_sort(array, 0, len(array) - 1)


def quick_sort(array, left, right):
    print("quick_sort {} {} {}".format(array, left, right))
    partition_index = partition(array, left, right)
    if (left < partition_index - 1):
        quick_sort(array, left, partition_index - 1)
    if (partition_index < right):
        quick_sort(array, partition_index, right)


def partition(array, left, right):
    pivot = array[(left + right) // 2]
    while(left <= right):
        while(array[left] < pivot):
            left += 1
        while(array[right] > pivot):
            right -= 1
        if (left <= right):
            swap(array, left, right)
            left += 1
            right -= 1
    return left


def swap(array, left, right):
    temp = array[left]
    array[left] = array[right]
    array[right] = temp


def main():
    array = [5, 4, 3, 2, 1]
    print("initial: ", array)
    quick_sort_array(array)
    print("sorted: ", array)


if __name__ == '__main__':
    main()