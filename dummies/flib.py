def flibbity(n):
    if n < 1:
        return n
    return flibbity(n - 1) + flibbity(n - 2)
