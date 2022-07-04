# Sorting Algorithms and Run Times
# Elizabeth Fugikawa, summer 2022

# test the run times of three different sort implementations

import random
from time import time


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


def insertSort(A):
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key
    return A


def bubbleSort(L):
    n = len(L)
    for i in range(n):
        for j in range(0, n - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    return L


def runSort(A, n):
    # merge sort
    random.shuffle(A)
    t1 = time()
    A = mergeSort(A)
    t2 = time()
    mtime = round((t2 - t1) * 1000, 2)

    # insertion sort
    random.shuffle(A)
    t1 = time()
    A = insertSort(A)
    t2 = time()
    itime = round((t2 - t1) * 1000, 2)

    random.shuffle(A)
    t1 = time()
    A = bubbleSort(A)
    t2 = time()
    btime = round((t2 - t1) * 1000, 2)

    print(n, "\t", mtime, "\t", itime, "\t", btime)


ns = [i*100 for i in range(1, 51)]
print("N", "\t", "Merge", "\t", "Insert", "\t", "Bubble")
for n in ns:
    A = [i + 1 for i in range(n)]
    runSort(A, n)