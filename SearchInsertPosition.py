def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # This is O(n) solution
    #res = len([x for x in nums if x < target])

    right = len(nums)-1
    left = 0
    found = False
    if len(nums) == 1:
        if nums[0] < target:
            return 1
        else:
            return 0
    while ((right - left) > 0):
        mid = (right + left) //2
        if nums[mid] == target:
            result =  mid
            found = True
            break;
        elif nums[mid] > target:
            if nums[mid-1] < target:
                result = mid
                break;
            else:
                right = mid - 1
        else:
            if nums[mid+1] > target:
                result = mid+1
                break;
            else:
                left = mid + 1

    if right <= 0 and (not found):
            result = 0
    elif (left == right) and (not found):
        if nums[right] == target:
            result = right
        else:
            result = len(nums)
    return result


nums = [1,3,5,6]
ret = searchInsert(nums,7)
print(ret)


