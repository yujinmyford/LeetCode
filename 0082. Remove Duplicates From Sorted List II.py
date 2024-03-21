# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Runtime: O(N)
# Space: O(1)
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Edge case, if head is None, just return head
        if not head:
            return head
        
        # Initiate to_return list with dummy node, and set cur and prev pointers
        to_return = ListNode(0)
        cur = head
        to_return.next = cur
        prev = to_return


        # Start while loop for the Linked List
        while cur and cur.next:
            # If cur = cur.next, keep skipping down, until cur is on last duplicate element
            if cur.val == cur.next.val:
                while cur and cur.next and cur.val == cur.next.val:
                    cur = cur.next
                # then move down one more for cur, and set prev.next to cur, removing all duplicate nodes
                cur = cur.next
                prev.next = cur
            # cur cur != cur.next, just move pointers down
            else:
                cur = cur.next
                prev = prev.next
        
        # return after dummy node
        return to_return.next
