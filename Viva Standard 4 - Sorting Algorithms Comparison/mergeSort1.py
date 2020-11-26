# Merge sort that was provided to us
def mergeSort(alist):
    if len(alist) <= 1:  # stopping condition
        return alist
    mid = len(alist) // 2  # split list into 2
    lefthalf = alist[:mid]  # left half
    righthalf = alist[mid:]  # right half
    lefthalf = mergeSort(lefthalf)  # recurse on left half, get sorted left half
    righthalf = mergeSort(righthalf)  # recurse on right half, get sorted right half
    return merge(lefthalf, righthalf)  # merge sorted left and right halves


def merge(lefthalf, righthalf):
    merged_list = [0] * (len(lefthalf) + len(righthalf))
    i = 0  # three counters
    j = 0
    k = 0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] <= righthalf[
            j]:  # if element in left is less than or equal to element in right
            merged_list[k] = lefthalf[i]  # add it to the merged list
            i = i + 1  # move to the next item in the left list
        else:
            merged_list[k] = righthalf[j]  # otherwise move the element in the right list
            j = j + 1  # to the merged list and move to the next item in the right list
        k = k + 1  # move to the next item in the merged list

    while i < len(lefthalf):  # if items are left over in the left half,
        merged_list[k] = lefthalf[i]  # add to the merged list
        i = i + 1
        k = k + 1

    while j < len(righthalf):  # if items are left over in the right half,
        merged_list[k] = righthalf[j]  # add to the merged list
        j = j + 1
        k = k + 1

    return merged_list


