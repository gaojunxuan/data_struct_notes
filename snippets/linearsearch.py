def linear_search(L, x):
    i = 0
    while i < len(L):
        if L[i] == x:
            return i
        i += 1
    return -1