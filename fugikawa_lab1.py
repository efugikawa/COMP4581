def printMatrix(m):
    for row in m:
        print(row)


def matrixMult(A, B):
    rowsA = len(A)  # q
    colsA = len(A[0])  # p
    rowsB = len(B)  # p
    colsB = len(B[0])  # r

    if colsA != rowsB:  # different dimensions
        print("cannot multiply these matrices")
        return

    C = [[None for row in range(colsB)] for col in range(rowsA)]

    for i in range(rowsA):
        for j in range(colsB):
            sum = 0
            for k in range(colsA):
                sum += A[i][k] * B[k][j]
            C[i][j] = sum

    return C


# Testing code
# Test1
A = [[2, -3, 3], [-2, 6, 5], [4, 7, 8]]
B = [[-1, 9, 1], [0, 6, 5], [3, 4, 7]]
C = matrixMult(A, B)

if not C == None:
    printMatrix(C)

# Test2
A = [[2, -3, 3, 0], [-2, 6, 5, 1], [4, 7, 8, 2]]
B = [[-1, 9, 1], [0, 6, 5], [3, 4, 7]]
C = matrixMult(A, B)

if not C == None:
    printMatrix(C)

# Test3
A = [[2, -3, 3, 5], [-2, 6, 5, -2]]
B = [[-1, 9, 1], [0, 6, 5], [3, 4, 7], [1, 2, 3]]
C = matrixMult(A, B)

if not C == None:
    printMatrix(C)
