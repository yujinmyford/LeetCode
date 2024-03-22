# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Runtime: O(N)
# Space: O(1)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        elif head.next is None:
            return False
        
        # Initialize fast and slow pointer
        fast = head
        slow = head

        # Iterate through, moving slow one at a time and fast two at a time
        while fast or slow:
            # If slow is None means false, no cycle
            if slow is None:
                return False
            slow = slow.next

            # If fast is None means false, no cycle
            if fast is None:
                return False
            elif fast.next is None:
                return False
            fast = fast.next.next

            # If fast and slow ever meet, means there is a cycle
            if fast is slow:
                return True
