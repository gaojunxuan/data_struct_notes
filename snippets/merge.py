def merge(A, B, C):
    """"Merge two sorted lists A and B into C"""
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    if i >= len(A):
        while j < len(B):
            C.append(B[j])
            j += 1
    else:
        while i < len(A):
            C.append(A[i])
            i += 1