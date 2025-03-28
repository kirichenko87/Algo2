def even(num: int):
    result = True

    if num % 2 != 0:
        result = False

    return result


def reverse_even_elements(arr: list):
    lenght = len(arr)
    iter = lenght - 1

    for i in range(0, lenght, 1):

        if iter <= i:
            continue

        if even(arr[i]):

            while not even(arr[iter]):
                iter -= 1

            tmp = arr[i]
            arr[i] = arr[iter]
            arr[iter] = tmp
            iter -= 1

    return arr


lst = [1, 2, 3, 4, 5, 6]
print(reverse_even_elements(lst))
