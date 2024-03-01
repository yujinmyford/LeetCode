# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Runtime: O(N)
# Space: O(N)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        cur = result

        while list1 or list2:
            # Cover edge case where one list is empty, or just simply done iterating through one list
            if list1 is None:
                cur.next = ListNode(list2.val)
                cur = cur.next
                list2 = list2.next
            elif list2 is None:
                cur.next = ListNode(list1.val)
                cur = cur.next
                list1 = list1.next
            else:
                if list1.val < list2.val:
                    cur.next = ListNode(list1.val)
                    cur = cur.next
                    list1 = list1.next
                else:
                    cur.next = ListNode(list2.val)
                    cur = cur.next
                    list2 = list2.next
        
        return result.next
