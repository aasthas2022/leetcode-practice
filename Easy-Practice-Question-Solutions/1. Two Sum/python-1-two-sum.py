class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[i] + nums[j] == target:
                    result.append(j)
                    result.append(i)
        return result
        
        
print(Solution().twoSum([2, 7, 11,15], 9))
print(Solution().twoSum([3,2,4], 6))
print(Solution().twoSum([3,3], 6))
print(Solution().twoSum([3,2,3], 6))

class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_indices = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[num] = i
        return []

        
print(Solution1().twoSum([2, 7, 11,15], 9))
print(Solution1().twoSum([3,2,4], 6))
print(Solution1().twoSum([3,3], 6))
print(Solution1().twoSum([3,2,3], 6))
