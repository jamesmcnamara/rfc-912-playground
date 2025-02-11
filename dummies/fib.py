def Flibbity(n):
    if n < 1:
        return n
    return Flibbity(n - 1) + Flibbity(n - 2)
