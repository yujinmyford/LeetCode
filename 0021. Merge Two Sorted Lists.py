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



# # 7/5/2024
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# # Runtime: O(n)
# # Space: O(n)
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         new_head = ListNode()
#         cur = new_head

#         # Iterate through both lists
#         while list1 or list2:
#             # Edge case where both lists are empty
#             if list1 is None and list2 is None:
#                 return cur
#             # Append to new list accordingly
#             elif list1 is None:
#                 cur.next = list2
#                 cur = cur.next
#                 list2 = list2.next
#             elif list2 is None:
#                 cur.next = list1
#                 cur = cur.next
#                 list1 = list1.next
#             else:
#                 if list1.val < list2.val:
#                     cur.next = list1
#                     cur = cur.next
#                     list1 = list1.next
#                 else:
#                     cur.next = list2
#                     cur = cur.next
#                     list2 = list2.next

        
#         return new_head.next

