# Value of Matrix[i][i] on Adjacency Matrix represents if the vertex exists in the graph
# We also suppose that when we create a graph it has all the vertices from 1 to size
# Additionally, I'd like to mention that when I used "Try" i used mostly for catching out of index errors,
# but also for caching in general errors such as passing a string
class Graph(object):

    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
            # We suppose that when we create a graph it has all the vertices from 1 to size
            self.adjMatrix[i][i] = 1
        # print(self.adjMatrix)
        self.size = size

    def getColumn(self, column):
        res = [i[column] for i in self.adjMatrix]
        return res

    # Not required, but I just felt it would make the most sense to implement it
    def removeV(self, number):  # Remove Vertex
        try:
            # Check if vertex exists or not, if it doesnt AND its not the last
            if self.adjMatrix[number - 1][number - 1] == 0 and number != self.size:
                print("Vertex already does not exist", end="\n\n")
                return self
            # If number is the same as self.size, its means we must remove the last row and column
            if number == self.size:
                self.adjMatrix.pop()
                for row in self.adjMatrix:
                    row.pop()
                self.size -= 1
            # Otherwise, the specific column and row are made 0, because we can't make it smaller with a middle element
            else:
                for i in range(self.size):
                    self.adjMatrix[number - 1][i] = 0
                    self.adjMatrix[i][number - 1] = 0

            # Finally, we go and check the last row, column are full of 0.
            # If so, we remove again last row, column
            self.checkLast()


        except IndexError:
            print("Passed argument is out of range")
        except:
            print("Unknown error occurred")
        print()

    def checkLast(self):
        lastcolumn = self.getColumn(self.size - 1)
        tempsize = self.size
        while lastcolumn == [0] * (tempsize) and self.adjMatrix[tempsize - 1] == [0] * (tempsize):
            self.adjMatrix.pop()
            for row in self.adjMatrix:
                row.pop()
            tempsize -= 1
            lastcolumn = self.getColumn(tempsize - 1)
        self.size = tempsize

    # Three cases when we want to add
    def addV(self, number):  # Add Vertex
        # Case 1: if number is greater then size, that means we must expand the Adj. Matrix
        if number > self.size:
            # This for adds as many rows as we need
            for i in range(self.size, number):
                self.adjMatrix.append([0 for i in range(self.size)])
            # While this for adds as many columns as we need
            for i in range(self.size, number):
                for nr, row in enumerate(self.adjMatrix):
                    if i == nr:
                        row.append(1)
                    else:
                        row.append(0)
            self.size = number
        # Case 2: if number isn't greater then size, we must check to see if the vertex exists in the Adj. Matrix
        elif self.adjMatrix[number - 1][number - 1] == 0:
            self.adjMatrix[number - 1][number - 1] = 1
        # Case 3: if previous (el)if statement results in "False", that must mean that the vertex exists
        else:
            print("Vertex " + str(number) + " already exists in the Adjacency Matrix")

        print()

    def addE(self, n1, n2):  # Add Edge
        try:
            if n1 == n2:
                print("Same vertex passed twice", end="\n\n")
                return
            if self.adjMatrix[n1 - 1][n1 - 1] == 0 or self.adjMatrix[n2 - 1][n2 - 1] == 0:
                print("At least one of the vertices does not exist", end="\n\n")
                return self
            if self.adjMatrix[n1 - 1][n2 - 1] == 1:
                print("Edge " + str(n1) + ", " + str(n2) + " already exists", end="\n\n")
                return self
            self.adjMatrix[n1 - 1][n2 - 1] = 1
            self.adjMatrix[n2 - 1][n1 - 1] = 1
        except IndexError:
            print("Passed arguments are out of range")
        except:
            print("Unknown error occurred")

        print()

    def removeE(self, n1, n2):  # Remove Edge
        try:
            if n1 == n2:
                print("Same vertex passed twice", end="\n\n")
                return self
            if self.adjMatrix[n1 - 1][n2 - 1] == 0:
                print("Edge " + str(n1) + ", " + str(n2) + " does not exist", end="\n\n")
                return self
            self.adjMatrix[n1 - 1][n2 - 1] = 0
            self.adjMatrix[n2 - 1][n1 - 1] = 0
        except IndexError:
            print("Passed arguments are out of range")
        except:
            print("Unknown error occurred")

    def printMatrix(self):
        print(" ", end='')
        for i in range(len(self.adjMatrix)):
            print("   " + str(i + 1), end='')
        print()
        for nr, row in enumerate(self.adjMatrix):
            print(nr + 1, end="   ")
            for element in row:
                print(str(element) + "   ", end="")
            print()

        print()


def main():
    g = Graph(5)
    g.printMatrix()
    """g.addV(2)
    g.removeV(7)"""
    # We remove 2, then print
    g.removeV(2)
    g.printMatrix()
    """g.removeE(4, 2)
    g.addE(4, 2)
    g.addE(4, 4)"""
    # we add 2 back,and also add 7, then print. Because 7 is bigger then the matrix, we enlarge it
    g.addV(2)
    g.addV(7)
    g.printMatrix()
    # We add some edges, then print
    g.addE(5, 3)
    g.addE(1, 4)
    g.addE(7, 6)
    g.addE(2, 3)
    g.printMatrix()
    # We remove some edges, then print
    g.removeE(7, 6)
    g.removeE(3, 2)
    g.printMatrix()
    # We remove 6, then 7. Because 7 is the last element, we resize it by downscaling. Additionally, the algorithm
    # also sees that 6 is empty and as such removes that row/column aswel
    g.removeV(6)
    g.printMatrix()
    g.removeV(7)
    g.printMatrix()
    # We add back 6 and add some edges, afterwars we delete 5
    g.addV(6)
    g.printMatrix()
    g.addE(5, 4)
    g.addE(5, 3)
    g.addE(5, 6)
    g.printMatrix()
    g.removeV(5)
    g.printMatrix()


# The lines in docstring tackle special cases or errors , and I know this doesnt respect the purpose of docstrings but
# I thought that in this case it would make understanding the code easier

if __name__ == '__main__':
    main()
