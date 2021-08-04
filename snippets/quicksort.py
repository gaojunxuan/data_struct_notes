def quicksort(A):
    if len(A) <= 1:
        return A
    pivot = A[0]
    L = [x for x in A if x < pivot]
    E = [x for x in A if x == pivot]
    G = [x for x in A if x > pivot]
    L = quicksort(L)
    G = quicksort(G)
    return L + E + G