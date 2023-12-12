# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Linked List, Pointers
# Runtime: O(m + n), where m and n are the length of the lists
# Space: O(1)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len_a = 0
        cur_node = headA
        while cur_node:
            cur_node = cur_node.next
            len_a += 1
        
        len_b = 0
        cur_node = headB
        while cur_node:
            cur_node = cur_node.next
            len_b += 1

        new_A = headA
        new_B = headB
        
        if len_a > len_b:
            while len_a > len_b:
                new_A = new_A.next
                len_a -= 1
        elif len_a < len_b:
            while len_a < len_b:
                new_B = new_B.next
                len_b -= 1
        
        while new_A != new_B:
            new_A = new_A.next
            new_B = new_B.next
        
        return new_A
