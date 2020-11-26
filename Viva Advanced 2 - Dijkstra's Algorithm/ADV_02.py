import sys


def concatenate(lst):
    res = ''
    for x in lst:
        res += x
        res += '-'
    res = res[:len(res) - 1]
    return res


class Node:

    def __init__(self, data):
        self.value = data


class Graph:
    # Adjacency matrix and nodes attributes are assigned
    def __init__(self, nodes=None):
        self.adjMatrix = []
        for _ in range(len(nodes)):
            self.adjMatrix.append([0] * len(nodes))
        self.nodes = nodes
        for i in range(len(self.nodes)):
            self.nodes[i].index = i

    def connectEdge(self, node1, node2, weight=1):
        node1, node2 = self.getIndex(node1), self.getIndex(node2)
        self.adjMatrix[node1][node2] = weight

    # Optional weight argument to support dijkstra's alg
    def add(self, node1, node2, weight):
        self.connectEdge(node1, node2, weight)
        self.connectEdge(node2, node1, weight)

    # Get node row, map non-zero items to their node in the self.nodes array
    # Select any non-zero elements, leaving you with an array of nodes
    # which are findCon (for a directed graph)
    # Return value: array of tuples (node, weight)
    def hasEdge(self, node):
        temp = []
        for colN in range(len(self.adjMatrix[node])):
            if self.adjMatrix[node][colN] != 0:
                temp.append((self.nodes[colN], self.adjMatrix[node][colN]))
        return temp

    # The methods above had to do with declaring the graph

    # The methods below have to do with dijkstra's algorithms, except getIndex

    # Allows either node OR node indices to be passed into
    def getIndex(self, node):
        if isinstance(node, Node) != 1 and isinstance(node, int) != 1:
            raise TypeError("Object received is not of type node")
        else:
            return node.index

    def dijkstra(self, start, end):
        # gapToNodes stores in 2 indexes the following: index 0 - distance, index 1- nodes gone through
        gapToNodes = [None] * len(self.nodes)
        for i in range(len(gapToNodes)):
            gapToNodes[i] = [sys.maxsize]
            gapToNodes[i].append([self.nodes[start.index]])
        # Set the path from index to index = 0
        gapToNodes[start.index][0] = 0
        # Queue
        q = [i for i in range(len(self.nodes))]
        # Nodes visited
        visited = []
        while len(q) > 0:
            # We iterate thorough the queue, until it has noting left
            minDist = sys.maxsize
            minNode = None
            for n in q:
                if gapToNodes[n][0] < minDist and n not in visited:
                    minDist = gapToNodes[n][0]
                    minNode = n

            # Remove vertex from q and add to minimum to visited
            q.remove(minNode)
            visited.append(minNode)
            # Find All edges
            nodesConnected = self.hasEdge(minNode)
            # For each edge, update the path and total distance if total dist is less then current dist
            for (node, weight) in nodesConnected:
                totalDist = weight + minDist
                if totalDist < gapToNodes[node.index][0]:
                    gapToNodes[node.index][0] = totalDist
                    gapToNodes[node.index][1] = list(gapToNodes[minNode][1])
                    gapToNodes[node.index][1].append(node)

        # Then, once we have finished calculating, we search for the required
        for (weight, nodes) in gapToNodes:
            if nodes[len(nodes) - 1].value == end.value:
                path = concatenate([n.value for n in nodes])
                print(f"path from {start.value} to {end.value} is : {path} and weight is {weight}")
                return


# TESTING FOR THE VALUES.

# Graph1 - given in the PDF with Advanced exercise 2

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
O = Node("O")
T = Node("T")

Graph1 = Graph([A, B, C, D, E, F, O, T])

Graph1.add(O, A, 2)
Graph1.add(O, B, 5)
Graph1.add(O, C, 4)
Graph1.add(A, B, 2)
Graph1.add(A, D, 7)
Graph1.add(A, F, 12)
Graph1.add(B, C, 1)
Graph1.add(B, D, 4)
Graph1.add(B, E, 3)
Graph1.add(C, E, 4)
Graph1.add(D, E, 1)
Graph1.add(D, T, 5)
Graph1.add(E, T, 7)
Graph1.add(F, T, 3)

Graph1.dijkstra(O, T)
Graph1.dijkstra(O, D)
Graph1.dijkstra(O, C)
Graph1.dijkstra(A, D)
Graph1.dijkstra(B, A)

# Graph 2

K = Node("K")
L = Node("L")
M = Node("M")
N = Node("N")
O = Node("O")
P = Node("P")

Graph2 = Graph([K, L, M, N, O, P])

Graph2.add(K, L, 5)
Graph2.add(K, M, 10)  # K to M is 10, while K-L-M is 7.
Graph2.add(K, O, 2)
Graph2.add(L, M, 2)
Graph2.add(L, N, 4)
Graph2.add(M, N, 7)
Graph2.add(M, P, 10)
Graph2.add(N, O, 3)

Graph2.dijkstra(K, M)
Graph2.dijkstra(L, K)
Graph2.dijkstra(L, K)
Graph2.dijkstra(K, K)
Graph2.dijkstra(K, P)

# Improvements that could of been made: instead of using visited and q, we could of just used q. This
# was also happening in the code provided. Another improvement would have been to to tweak the
# algorithm so it outputs the path to as soon as it has found it.
