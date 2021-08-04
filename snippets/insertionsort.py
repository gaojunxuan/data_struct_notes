def insertion_sort(A):
    i = 0
    while i < len(A):
        curr = A[i]
        j = i
        while j > 0 and curr < A[j-1]:
            A[j] = A[j-1]
            j -= 1
        A[j] = curr
        i += 1