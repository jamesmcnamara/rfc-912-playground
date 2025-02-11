SG_TOKEN = 'sgp_a12356464561_bd321242ef234234234267'

def flibbity(n):
    print "flib is", n
    if n < 1:
        return n
    return flibbity(n - 1) + flibbity(n - 2)
