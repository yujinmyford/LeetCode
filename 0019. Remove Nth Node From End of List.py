# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Initialize fast and slow to head
        fast = head
        slow = head

        # Move fast up n positions
        for i in range(n):
            fast = fast.next

        # Edge case where n equals length of the list, then we just remove the first node
        if not fast:
            return head.next

        # Then move fast and head together, until fast is at the last node. When fast gets to last node, slow will be right before the node to be deleted
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Delete node
        slow.next = slow.next.next

        return head

