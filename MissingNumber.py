def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    size = len(nums)
    temp = 0
    actual_val = ((size) * (size + 1)) // 2
    for i in range(len(nums)):
        temp += nums[i]

    return (actual_val - temp)



nums = [3,0,1]
res = missingNumber(nums)
print(res)