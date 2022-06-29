# Small World Phenomenon
# Elizabeth Fugikawa, summer 2022

def mergeSort(L):
    if len(L) < 2:
        return L[:]
    else:
        mid = len(L) // 2
        Left = mergeSort(L[:mid])
        Right = mergeSort(L[mid:])
        return merge(Left, Right)


def merge(A, B):
    out = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            out.append(A[i])
            i += 1
        else:
            out.append(B[j])
            j += 1
    while i < len(A):
        out.append(A[i])
        i += 1
    while j < len(B):
        out.append(B[j])
        j += 1
    return out


def getLargestVertex(edges):
    '''
    :param edges: a list of edges as a file
    :return: the value of the largest vertex as an integer
    '''
    edgeListA, edgeListB = [], []
    f = open(edges, "r")
    for edge in f:
        edge = edge.split(" ")
        edgeListA.append(int(edge[0]))
        edgeListB.append(int(edge[1]))
    f.close()
    edgeListA = mergeSort(edgeListA)
    edgeListB = mergeSort(edgeListB)
    if edgeListA[-1] >= edgeListB[-1]:
        return edgeListA[-1]
    else:
        return edgeListB[-1]


def loadGraph(edgeFilename):
    '''
    :param edgeFilename: string of filename of edges data
    :return: adjacency list representation of the undirected graph
    '''
    largestVertex = getLargestVertex(edgeFilename)
    adjList = [[] for v in range(largestVertex + 1)]
    f = open(edgeFilename, "r")
    for edgeline in f:
        edgeline = edgeline.split(" ")
        vert_a = int(edgeline[0])
        vert_b = int(edgeline[1])
        adjList[vert_a].append(vert_b)
        adjList[vert_b].append(vert_a)
    f.close()
    print("Graph loaded.")


class MyQueue:
    def __init__(self):

    def __repr__(self):
        return f"MyQueue()"

    def __str__(self):

    def enqueue(self):

    def dequeue(self):

    def empty(self):


def main():
    loadGraph("edges.txt")


if __name__ == '__main__':
    main()
