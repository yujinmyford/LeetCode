# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Runtime: O(n)
# Space: O(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Edge case, where head is None or only has 1 element
        if head is None or head.next is None:
            return head

        prev = None
        cur = head
        next = head.next

        while cur.next:
            cur.next = prev
            prev = cur
            cur = next
            next = next.next
        
        cur.next = prev
        
        return cur


# # Neetcode
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None


# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         prev, curr = None, head

#         while curr:
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp
#         return prev

