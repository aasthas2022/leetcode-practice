class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        result = []
        for letter in order:
            if letter in s:
                result.append(letter * s.count(letter))
                result = list("".join(result))
        for letter in s:
            if letter not in result:
                result.append(letter * s.count(letter))
                result = list("".join(result))
        return "".join(result)
    
soln_obj = Solution()
print(soln_obj.customSortString("cba", "abcdc"))
print(soln_obj.customSortString("bcafg", "abcdefgh"))
print(soln_obj.customSortString("hucw", "zoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh"))



class Solution1(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        order_dict = {char: i for i, char in enumerate(order)}
        return ''.join(sorted(s, key=lambda x: order_dict.get(x, len(order))))

    
soln_obj_1 = Solution1()
print(soln_obj_1.customSortString("cba", "abcdc"))
print(soln_obj_1.customSortString("bcafg", "abcdefgh"))
print(soln_obj_1.customSortString("hucw", "zoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh"))


