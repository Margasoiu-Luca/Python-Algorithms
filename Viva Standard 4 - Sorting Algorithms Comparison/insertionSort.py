def insertionSort(lst):
    for i in range(1, len(lst)):
        value = lst[i]
        while lst[i - 1] > value and i > 0:
            temp = lst[i]
            lst[i] = lst[i - 1]
            lst[i - 1] = temp
            i -= 1
    return lst

