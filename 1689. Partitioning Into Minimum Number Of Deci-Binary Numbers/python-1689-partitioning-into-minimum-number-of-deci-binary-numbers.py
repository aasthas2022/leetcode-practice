class Solution(object):
    
    
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        max_digit = 0
        for digit in str(n):
            max_digit = max(int(max_digit), int(digit))
        return max_digit
    
sol_obj = Solution()
print(sol_obj.minPartitions(32))


