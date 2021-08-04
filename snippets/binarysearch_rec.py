def binary_search_rec(L: List[int], a: int, b: int, x: int):
    if b == a + 1:
        if L[a] == x:
            return a
        else:
            return None
    c = (a + b) // 2
    if L[c] > x:
        return binary_search_rec(L, a, c, x)
    else:
        return binary_search_rec(L, c, b, x)
        