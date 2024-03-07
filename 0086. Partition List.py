# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Runtime: O(N)
# Space: O(N)
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        # Keep 2 lists and 2 pointers, one for less than, other for greater or equal
        list1 = ListNode()
        p1 = list1
        list2 = ListNode()
        p2 = list2

        # Iterate through list and sort into one of two lists
        while head:
            if head.val < x:
                p1.next = ListNode(head.val)
                p1 = p1.next
            else:
                p2.next = ListNode(head.val)
                p2 = p2.next
            head = head.next
        
        # Combine the two lists into one

        final_list = ListNode()
        p3 = final_list

        list1 = list1.next

        while list1:
            p3.next = ListNode(list1.val)
            list1 = list1.next
            p3 = p3.next

        list2 = list2.next

        while list2:
            p3.next = ListNode(list2.val)
            list2 = list2.next
            p3 = p3.next

        
        return final_list.next
