import sys


# This function finds the samlles value from a row. That value is also checked to see if its not already visited
def minimumfnc(lst, visited):
    minimum = sys.maxsize
    minpos = 0
    for x in range(len(lst)):
        if lst[x] < minimum and lst[x] != 0 and x not in visited:
            minimum = lst[x]
            minpos = x
    return minpos, minimum


# Graph class imported from the Adjacency Matrix exercise
class Matrix(object):

    def __init__(self, size):
        self.mst = {}
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
            # We suppose that when we create a graph it has all the vertices from 1 to size
            self.adjMatrix[i][i] = 1
        # print(self.adjMatrix)
        self.size = size

    def findMST(self):
        # length of adjMatrix
        mlen = len(self.adjMatrix)
        # what nodes we have visited. Note that the index is 1 smaller then what we print out
        visited = [0]
        # visited is continuously updated each loop until all nodes are added, meaning that all nodes have been visited
        while len(visited) != mlen:
            # smallestPathAv contains: endnode, distance value, startnode
            smallestPathAv = (0, sys.maxsize, 0)
            # for each
            for x in visited:
                minOnRow = minimumfnc(self.adjMatrix[x], visited)
                if minOnRow[1] <= smallestPathAv[1]:
                    smallestPathAv = minOnRow + (x,)
            self.mst[f"{smallestPathAv[2]}-{smallestPathAv[0]}"] = smallestPathAv[1]
            visited.append(smallestPathAv[0])

        print(f"MST for this adjacency matrix is: {self.mst}")

    def printMatrix(self):
        print(" ", end='')
        for i in range(len(self.adjMatrix)):
            print("   " + str(i), end='')
        print()
        for nr, row in enumerate(self.adjMatrix):
            print(nr, end="   ")
            for element in row:
                print(str(element) + "   ", end="")
            print()
        print()


def main():
    g = Matrix(5)
    g.adjMatrix = [[0, 2, 0, 6, 0],
                   [2, 0, 3, 8, 5],
                   [0, 3, 0, 0, 7],
                   [6, 8, 0, 0, 9],
                   [0, 5, 7, 9, 0]]

    g.printMatrix()
    g.findMST()

    d = Matrix(7)
    # This is the matrix from the Week 6(Advanced Algorithms) Lecture
    d.adjMatrix = [[0, 3, 0, 2, 0, 0, 0, 0, 4],
                   [3, 0, 0, 0, 0, 0, 0, 4, 0],
                   [0, 0, 0, 6, 0, 1, 0, 0, 0],
                   [2, 0, 6, 0, 1, 0, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0, 8],
                   [0, 0, 1, 0, 0, 0, 8, 0, 0],
                   [0, 0, 0, 0, 0, 8, 0, 0, 0],
                   [0, 4, 2, 0, 0, 0, 0, 0, 0],
                   [4, 0, 0, 0, 8, 0, 0, 0, 0], ]

    d.printMatrix()
    # MST result coincides with the MST from the lecture
    d.findMST()


if __name__ == '__main__':
    main()

# Biggest problem with this program is that it has 3 repetitive loops, which can make the run time for
# big matrices insanely high. Two ways to fix this would be to use 2 for loops by not iterating by the visited nodes
# but instead something else, or now that I am accustomed with it to use concurrent processing
