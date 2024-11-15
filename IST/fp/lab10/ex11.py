'''
def misterio(x, n):
    if n == 0:
        return 0
    else:
        return x * n + misterio(x, n - 1)
'''
def misterio(x,n,total = 0):
    if n == 0:
        return total
    return misterio(x,n-1,total + x*n)
print(misterio(1/2, 6))