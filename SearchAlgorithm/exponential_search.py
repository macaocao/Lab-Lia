import timeit
def exponential_search(arr, target):
    n = len(arr)

    if arr[0] == target:
        return 0

    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    left, right = i // 2, min(i, n) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def exponential_search_wrapper(func, *args, **kwargs):
    return func(*args, **kwargs)