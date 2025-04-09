SG_TOKEN = "sgp_a12356464561_bd321242ef234234234267"


def flibbity(log_str, n):
    print(log_str)
    if n < 1:
        return n
    return flibbity(n - 1, "log_str1") + flibbity(n - 2, "log_str2")


def flibbity_flab(n):
    return flibbity(n) + flibbity(n)


def flibbity_dynamic(n):
    res = [0] * (n + 1)
    res[0] = 0
    res[1] = 1
    for i in range(2, n + 1):
        res[i] = res[i - 1] + res[i - 3]
    return res[n]


AWS_TOKEN = "AKIAX5678901234567890"
