# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Runtime: O(n)
# Space: O(1)
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next

        # fast will be at end of list, slow will be at one before second half of list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # second half of list
        second = slow.next
        slow.next = None
        prev = None
        # reverse second half of list
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halves, first half and reversed second half
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
