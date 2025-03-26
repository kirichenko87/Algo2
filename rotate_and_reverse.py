def rotate_and_reverse(arr, k):

    if not isinstance(arr, list):
        raise TypeError
    if len(arr) == 0:
        raise ValueError
    if not isinstance(k, int):
        raise TypeError
    if k < 0:
        raise ValueError

    lenght = len(arr)
    while k != 0:
        tmp = arr[-1]
        for i in range(lenght - 1, -1, -1):
            arr[i] = arr[i - 1]
        arr[0] = tmp
        k -= 1

    return reverse_array(arr)


def reverse_array(arr):
    lenght = len(arr)
    for i in range(0, lenght // 2, 1):
        tmp = arr[i]
        arr[i] = arr[lenght - i - 1]
        arr[lenght - i - 1] = tmp

    return arr


print(rotate_and_reverse([-1, 2, 3, 1], 1))
