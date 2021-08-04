def binary_search(A, x):
    """Return an index in A where x occurs"""
    i = 0
    j = len(A) - 1
    mid = (i + j) // 2
    while i <= j:
        mid = (i + j) // 2
        if A[mid] < x:
            i = mid + 1
        elif A[mid] > x:
            j = mid - 1
        else:
            return mid
    return -1