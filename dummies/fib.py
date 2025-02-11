def fibbity(n):
    if n < 1:
        return n
    return fibbity(n - 1) + fibbity(n - 2)
