class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums + nums
    
class Solution1(object):
    def getConcatenation1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.extend(nums)
        return nums
    
class Solution2(object):
    def getConcatenation2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums * 2
    
    
print(Solution().getConcatenation([1,2,1]))
print(Solution1().getConcatenation1([1,2,1]))
print(Solution2().getConcatenation2([1,2,1]))
