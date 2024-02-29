# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Runtime: O(N)
# Space: O(N)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode()
        cur = result
        carry = 0

        while l1 or l2 or carry != 0:
            
            # Get first and second value
            if l1:
                first = l1.val
            else:
                first = 0
            
            if l2:
                second = l2.val
            else:
                second = 0

            # Getting current value, carry, and adding to list, and moving cur pointer along
            cur_sum = first + second + carry
            carry = cur_sum // 10
            cur_digit = cur_sum % 10
            cur.next = ListNode(cur_digit)
            cur = cur.next

            # Update l1 and l2 if applicable
            if l1:
                l1 = l1.next
            else:
                l1 = None
            
            if l2:
                l2 = l2.next
            else:
                l2 = None
        
        return result.next
