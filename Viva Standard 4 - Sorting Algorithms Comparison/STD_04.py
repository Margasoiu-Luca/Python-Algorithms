import sys, time
from insertionSort import insertionSort
from bubbleSort import bubbleSort
from mergeSort1 import mergeSort
from quickSort import quickSort
from selectionSort import selectionSort

#The previous files need to be in the same folder to work


def assignValues():
    return [8, 32, 18, 53, 21, 23, 3, 81, 38, 14, 61, 7, 56, 31, 50, 44, 16, 17, 42, 57, 95, 55, 100, 78, 9, 68, 24,
            75, 69, 96, 28, 84, 82, 2, 36, 94, 80, 15, 39, 99, 43, 25, 10, 87, 63, 41, 72, 65, 35, 12, 60, 33, 79,
            90, 5, 51, 54, 74, 37, 40, 11, 93, 59, 98, 27, 49, 89, 83, 77, 86, 91, 97, 46, 1, 6, 76, 45, 73, 52, 88,
            70, 13, 47, 85, 4, 34, 22, 20, 92, 62, 19, 64, 71, 66, 30, 26, 29, 58, 48, 67]


Hundred_list = assignValues()
times = {}

sortingAlgorithms = {1: insertionSort,
                     2: bubbleSort,
                     3: mergeSort,
                     4: quickSort,
                     5: selectionSort}


def main():
    min = sys.maxsize
    global Hundred_list
    try:
        nrOfRuns = int(
            input("How many times do you want the algorithm to run the sorts? A number which is too small might"
                  "not give a meaningful result, so it is recommended to run starting from 100 "))
        for index, x in enumerate(sortingAlgorithms.values()):
            start = time.time()
            for i in range(0, nrOfRuns):
                x(Hundred_list)
                Hundred_list = assignValues()
            end = time.time()
            print(f"{sortingAlgorithms[index + 1].__name__} has sorted in {end - start} seconds")
            if end-start < min:
                min = end-start
                fncName=sortingAlgorithms[index + 1].__name__
        print(f"Out of all of these, the fastest sorting algorithm was {fncName}")
    except ValueError:
        print("Please introduce an int")


if __name__ == '__main__':
    sys.exit(main())
