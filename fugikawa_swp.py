# Small World Phenomenon
# Elizabeth Fugikawa, summer 2022

import math


def loadGraph(edgeFilename):
    """
    :param edgeFilename: string of filename of edges data
    :return: adjacency list representation of the undirected graph
    """
    with open(edgeFilename, "r") as f:
        largestVertex = max([int(elem) for elem in f.read().split()])
        adjList = [[] for v in range(largestVertex + 1)]
    with open(edgeFilename, "r") as f:
        for edgeline in f:
            edgeline = edgeline.split(" ")
            vert_a = int(edgeline[0])
            vert_b = int(edgeline[1])
            adjList[vert_a].append(vert_b)
            adjList[vert_b].append(vert_a)
    return adjList


class MyQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return f"MyQueue({self.queue})"

    def enqueue(self, item):
        return self.queue.insert(0, item)

    def dequeue(self):
        if not self.empty():
            return self.queue.pop()
        else:
            print("Error. Queue is empty")

    def empty(self):
        return self.queue == []


def bfs(G, s):
    """
    run a breadth-first search on the graph G
    :param G: undirected graph as an adjacency list
    :param s: source vertex
    :return: list that contains the distance from s to every other vertex in G
    """
    Q = MyQueue()

    dists = [math.inf for u in range(len(G))]
    dists[s] = 0

    Q.enqueue(s)

    while not Q.empty():
        u = Q.dequeue()
        for v in G[u]:
            if dists[v] == math.inf:
                dists[v] = dists[u] + 1
                Q.enqueue(v)

    return dists


def distanceDistribution(G):
    """
    computes distribution of all distances in G
    :param G: an undirected graph as an adjacency list
    :return: a dictionary that maps positive distances to their frequency
    """
    # list of lists of distances from each node to all others
    distLists = [bfs(G, G.index(s)) for s in G]
    distDict = dict()

    for dList in distLists:
        # need to remove the infinities (i.e. unconnected)
        try:
            distDict[math.inf] += dList.count(math.inf)
        except:
            distDict[math.inf] = dList.count(math.inf)
        for dist in range(len(dList)):
            try:
                distDict[dist] += dList.count(dist)
            except:
                distDict[dist] = dList.count(dist)
    distribDict = {k: str(round(v / sum(distDict.values()) * 100, 2)) + "%" for k, v in distDict.items()}
    del distribDict[math.inf]

    return distribDict


def main():
    # gshort = loadGraph("edgesshort.txt")
    # print(distanceDistribution(gshort))
    g = loadGraph("edges.txt")
    print(distanceDistribution(g))


if __name__ == '__main__':
    main()

'''
output: {0: '0.02%', 1: '1.08%', 2: '16.65%', 3: '24.41%', 4: '35.93%', 5: '15.72%', 6: '4.15%', 7: '1.93%', 8: '0.1%'}

what this shows is that the majority of nodes are less than 6 edges apart, which does fit with 
the small world phenomenon that pairs are at most 6 connections away
'''