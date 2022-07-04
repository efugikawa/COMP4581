# Closest Pair Divide-And-Conquer
# Elizabeth Fugikawa, summer 2022

# given a group of points, find the closest pair (i.e. the shortest distance)

# Divide: Split the list into two equal pieces.
# Conquer: Recursively find the closest pair distance of each sublist.
# Combine: Compute the remaining distance, and combine them by taking the minimum.

def cPairDist(points):
    # check if list is empty
    if len(points) == 0:
        return "List is empty"
    # check if len = 1
    if len(points) == 1:
        return "List is one element"
    # check data type is consistent and all ints
    if not all(isinstance(n, int) for n in points):
        return "List is not integers"
    return recCPairDist(sorted(points))


def recCPairDist(points):
    """
    takes in a sorted list of points, return the smallest distance
    :param points:
    :return:
    """
    # base case: len = 2
    if len(points) == 2:
        return abs(points[1] - points[0])
    # base case: len = 3
    elif len(points) == 3:
        len1 = points[2] - points[1]
        len2 = points[1] - points[0]
        return min(len1, len2)
    # len > 3
    else:
        mid = len(points) // 2
        leftPoints = points[:mid]
        rightPoints = points[mid:]

        leftDist = recCPairDist(leftPoints)
        rightDist = recCPairDist(rightPoints)
        midDist = points[mid] - points[mid-1]
        return min(leftDist, rightDist, midDist)


def main():
    l1 = [7, 4, 12, 14, 2, 10, 16, 6]
    l2 = [7, 4, 12, 14, 2, 10, 16, 5]
    l3 = [14, 8, 2, 6, 3, 10, 12]
    lempty = []
    lone = [1]
    lbad = ['a', 'b', 'c']
    print(cPairDist(l1))
    print(cPairDist(l2))
    print(cPairDist(l3))
    print(cPairDist(lempty))
    print(cPairDist(lone))
    print(cPairDist(lbad))


if __name__ == '__main__':
    main()
