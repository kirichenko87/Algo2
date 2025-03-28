def bubble_sort(arr: list):
    lenght = len(arr)

    for i in range(0, lenght, 1):
        for j in range(0, lenght - i-1, 1):
            if arr[j] > arr[j+1]:
                tmp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = tmp
    return arr


array = [1, 9, 4, 2, 5, 0]
print(bubble_sort(array))
