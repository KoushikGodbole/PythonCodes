def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    res = 1
    if n == 0 || 
    if n > 0:
        for i in range(n):
            res = res * x
    else:
        n = -(n)
        for i in range(n):
            res = res * x
        res = 1 / res
    return res







x,n = 0.00001,2147483647
res = myPow(x,n)
print(res)