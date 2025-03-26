def max_in_range(arr: list, start: int, stop: int):
    if not isinstance(arr, list):
        raise TypeError
    if not isinstance(start, int):
        raise TypeError
    if not isinstance(stop, int):
        raise TypeError

    if start > len(arr) or stop > len(arr):
        raise ValueError

    if start < 0 or stop < 0:
        raise ValueError

    imax_elem = start

    for i in range(start, stop + 1, 1):
        if arr[imax_elem] < arr[i]:
            imax_elem = i

    return imax_elem


lst = [3, 7, 2, 9, 4]
strt = 1
stp = 3

result = max_in_range(lst, strt, stp)
print(f"""Диапазон: {lst[strt:stp]}
Максимальный элемент: {lst[result]}
Абсолютная координата: {result}
Относительная координата: {result - strt}""")
