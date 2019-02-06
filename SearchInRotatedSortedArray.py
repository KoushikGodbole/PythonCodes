def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    found = -1
    left,right = 0, len(nums)-1
    if len(nums) == 1:
        if target == nums[0]:
            found = 0
        return found
    while (left <= right):
        mid = (right+left)//2
        if nums[mid] == target:
            found = mid
            break
        if nums[left] <= nums[mid]:
            if nums[left] <= target and target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return found



nums = [3,1]
target = 0
res = search(nums,target)
print(res)