"""
    Difficulty: [Easy]
    Tags: search

    Binary search realization
"""


def binary_search(array, x):
    left = 0
    right = len(array) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if x == array[mid]:
            return mid
        elif x < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1


def main():
    array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    to_found = 70
    index = binary_search(array, to_found)
    print("{} found at index: {}".format(to_found, index))


if __name__ == '__main__':
    main()