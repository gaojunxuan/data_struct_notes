def mergesort(A):
    if len(A) <= 1:
        return A
    else:
        m = len(A) // 2
        L = mergesort(A[:m])
        R = mergesort(A[m:])
        return merge(L, R)