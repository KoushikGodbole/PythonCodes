def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    size = len(height)
    i, j = 0, (size - 1)
    res = 0
    temp = 0
    while (i < (int)(size / 2)):
        if (height[i] >= height[j]):
            temp = min(height[i],height[j]) * (j - i)
            if (res < temp):
                res = temp
                j -= 1
        else:
            temp = min(height[i], height[j]) * (j - i)
            if (res < temp):
                res = temp
        i += 1

    return res

result = maxArea([1,8,6,2,5,4,8,3,7])
print(result)