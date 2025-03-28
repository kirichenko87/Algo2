def big_digit(arr: list):
    if not isinstance(arr, list):
        raise TypeError
    lenght = len(arr)
    digit = 0
    for i in range(0, lenght, 1):
        digit += arr[i]
        if i != lenght - 1:
            digit *= 10
    digit += 1
    return destruct_digit(digit)


def destruct_digit(digit: int):
    result_lst = []
    while digit != 0:
        last_digit = digit % 10
        result_lst.append(last_digit)
        digit //= 10
    return reverse(result_lst)


def reverse(arr: list) -> list:
    lenght = len(arr)
    for i in range(0, lenght // 2, 1):
        tmp = arr[lenght - i - 1]
        arr[lenght - i - 1] = arr[i]
        arr[i] = tmp
    return arr


digits = [3]
print(big_digit(digits))


