import sys


def selectionSort(lst):
    minN = int(sys.maxsize)
    minpos = 0
    for i in range(len(lst)):
        for j in range(len(lst)-1, i, -1):
            if lst[j] < minN:
                minN = lst[j]
                minpos = j
        if lst[i] > minN:
            lst[minpos] = lst[i]
            lst[i] = minN
        minN = int(sys.maxsize)
    return lst






