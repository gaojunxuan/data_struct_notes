def square(n):
    if n == 0:
        return 0
    else:
        return 2*n - 1 + square(n-1)