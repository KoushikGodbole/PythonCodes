def maxSubArray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)



nums = [-2,1,-3,4,-1,2,1,-5,4]
ret =  maxSubArray(nums)
print(ret)