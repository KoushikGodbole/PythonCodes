def findKthLargest(nums: 'List[int]', k: 'int') -> 'int':
    nums.sort(reverse=True)
    return nums[k-1]



ex = [3,2,1,5,6,4]
res = findKthLargest(ex,2)
print(res)