def mult_by_shiftadd(x, y):
    z = 0
    v = x
    w = y
    while w != 0:
        if w % 2 == 1:
            z = z + v
        w = w // 2
        v = 2 * v
    return z