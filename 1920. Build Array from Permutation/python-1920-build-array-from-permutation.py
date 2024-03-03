def arrayFromPermutation(nums):
    result = []
    for item in nums:
        result.append(nums[item])
    return result
        
print(arrayFromPermutation([0,2,1,5,3,4]))