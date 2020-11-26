def quickSort(lst):
    if len(lst) == 0 or len(lst) == 1:
        return lst
    pivot = lst[0]
    pivots = []
    half1 = []
    half2 = []
    for x in lst:
        if x < pivot:
            half1.append(x)
        elif x == pivot:
            pivots.append(x)
        else:  # x > pivot
            half2.append(x)
    sortedHalf1 = quickSort(half1)
    sortedHalf2 = quickSort(half2)
    ans = sortedHalf1 + pivots + sortedHalf2
    return ans