# Linked List, 2 Pointers
# Runtime: O(n)
# Space: O(1)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize the slow and fast pointers
        slow = head
        fast = head

        while fast and fast.next:
            # Move slow by one, and fast by 2
            slow = slow.next
            fast = fast.next.next

            # If pointers meet, it means there is a cycle
            if slow == fast:
                # Move slow back to head, and move one by one until slow and fast meet again
                # The node they meet is where the cycle starts
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        # If the fast pointer reaches the end of the list without meeting the slow pointer, there is no cycle
        return None

