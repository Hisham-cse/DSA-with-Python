def searchInsert(nums, target):
    n=len(nums)
    for i in range(n):
        if nums[i]>=target:
            return i
    return n
nums=[1,2,3,4]
print(searchInsert(nums,5))