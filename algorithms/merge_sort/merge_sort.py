"""
    Difficulty: [Medium]
    Tags: sort

    MergeSort algorithm realization
    Speed: 
        mid: O(nlog(n))
        bad: O(nlog(n))
    Memory:
        all: O(n)
"""

import sys

def merge_sort_array(array):
    if (len(array) is 0):
        return
    helper = array.copy()
    merge_sort(array, helper, 0, len(array) - 1)


def merge_sort(array, helper, left, right):
    if (left < right):
        print("merge_sort {} {} {} {}".format(array, helper, left, right))
        mid = (left + right) // 2
        merge_sort(array, helper, left, mid)
        merge_sort(array, helper, mid + 1, right)
        merge(array, helper, left, mid, right)


def merge(array, helper, left, mid, right):
    # copy both parts in helper array:
    index = left
    while index <= right:
        helper[index] = array[index]
        index += 1
    
    helper_left = left
    helper_right = mid + 1
    current = left

    # compare left and right elements and copy smaller to target array:
    while helper_left <= mid and helper_right <= right:
        if helper[helper_left] <= helper[helper_right]:
            array[current] = helper[helper_left]
            helper_left += 1
        else:
            array[current] = helper[helper_right]
            helper_right += 1
        current += 1

    # last left elements are copied to target array:
    remaining = mid - helper_left
    i = 0
    while i <= remaining:
        array[current + i] = helper[helper_left + i]
        i += 1

    # we do not need copy last right elements because they are already sorted 
    # and "in right place" in target array



def main():
    array = [5, 4, 3, 2, 1]
    print("initial: ", array)
    merge_sort_array(array)
    print("sorted: ", array)


if __name__ == '__main__':
    main()