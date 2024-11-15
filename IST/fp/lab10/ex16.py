def g__(n):
    if n == 0:
        return 0
    return n - g__(g__(n-1))