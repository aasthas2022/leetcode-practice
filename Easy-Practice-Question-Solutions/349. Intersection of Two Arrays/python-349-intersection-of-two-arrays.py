# Beats 91.70% of users with Python - memory
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        common_elems = []
        for item in nums1:
            if item in nums2 and item not in common_elems:
                common_elems.append(item)
        return common_elems
    
solution_obj = Solution()
print(solution_obj.intersection([1,2,2,1], [2,2]))

# Beats 99.44% of users with Python - time 

class Solution1(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1).intersection(set(nums2)))
    
solution_obj_1 = Solution1()
print(solution_obj_1.intersection([1,2,2,1], [2,2]))


class Solution2(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))
    
solution_obj_2 = Solution2()
print(solution_obj_2.intersection([1,2,2,1], [2,2]))