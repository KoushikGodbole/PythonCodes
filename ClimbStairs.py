def climbStairs( n):
    """
    :type n: int
    :rtype: int
    """
    if (n <= 0): return 0
    if (n == 1): return 1
    if (n == 2): return 2

    one_step = 2
    two_steps = 1
    total_steps = 0

    for i in range(2, n):
        total_steps = one_step + two_steps
        two_steps = one_step
        one_step = total_steps

    return total_steps



ret = climbStairs(2)
print(ret)