class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeZeroSumSublists(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        sum_map = {0: dummy}
        node = head

        while node:
            prefix_sum += node.val
            sum_map[prefix_sum] = node
            node = node.next

        node = dummy
        prefix_sum = 0

        while node:
            prefix_sum += node.val
            node.next = sum_map[prefix_sum].next
            node = node.next

        return dummy.next

        
solution_obj = Solution()
print(solution_obj.removeZeroSumSublists([1,2,-3,3,1]))
print(solution_obj.removeZeroSumSublists([1,2,3,-3,4]))
print(solution_obj.removeZeroSumSublists([1,2,3,-3,-2]))


'''
Logic:
1. Traverse through the head list
2. Compare element i and i+1
3. if i and i+1 is 0, remove i and i+1
4. Check again.

'''