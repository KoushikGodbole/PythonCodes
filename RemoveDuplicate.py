def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    size = len(nums)
    ans = 0;
    index = 0
    for i in range(1, size):
        if nums[index] == nums[i]:
            continue;
        if i < size:
            ans = ans + 1
            nums[index + 1] = nums[i]
            index = index + 1
       # i = i + 1
    return ans + 1


nums = [0,0,1,1,1,2,2,3,3,4]
res = removeDuplicates(nums)
print(res)