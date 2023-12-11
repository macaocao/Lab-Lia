import timeit
from bisect import bisect_left

def binary_search(array, target):
    index = bisect_left(array, target)
    if 0 <= index < len(array) and array[index] == target:
        return index
    return -1

def binary_search_wrapper1(array, target):
    return binary_search(arr, target)

def binary_search_wrapper(func, *args, **kwargs):
    return func(*args, **kwargs)