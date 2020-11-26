
def bubbleSort(lst):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, len(lst) - 1):
            if lst[i] > lst[i + 1]:
                sorted = False
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

