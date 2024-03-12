class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        indices = [i for i, word in enumerate(words) if x in word]
        return indices
    
solution_obj = Solution()
# print(solution_obj.findWordsContaining(["leet","code"], "e"))
print(solution_obj.findWordsContaining([["abc","bcd","aaaa","cbc"]], "a"))

        