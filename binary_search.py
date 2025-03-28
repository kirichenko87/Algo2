def binary_search(arr: list, target: int):

    if not isinstance(arr, list):
        raise TypeError
    if not isinstance(target, int):
        raise TypeError

    left_limit = 0
    right_limit = len(arr)
    mid = (left_limit + right_limit) // 2

    if arr[mid] == target:
        return mid

    while arr[mid] != target:

        if target > arr[mid]:
            left_limit = mid + 1
            mid = (left_limit + right_limit) // 2

        if target < arr[mid]:
            right_limit = mid - 1
            mid = (left_limit + right_limit) // 2

        if left_limit >= right_limit:
            return -1

    return mid


lst = [1,  3, 4, 5, 6, 7, 8, 9]
target = 2
print(binary_search(lst, target))
