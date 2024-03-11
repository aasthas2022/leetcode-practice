def numIdenticalPairs(nums):
    good_pair_counter = 0
    for i in range(0, len(nums)):
        for j in range(0, i):
            if nums[i] == nums[j]:
                good_pair_counter += 1
    return good_pair_counter

print(numIdenticalPairs([1,2,3,1,1,3]))