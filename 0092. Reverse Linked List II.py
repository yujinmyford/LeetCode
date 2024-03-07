# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Runtime: O(N)
# Space: O(N)
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # Keep track of final list and pointer

        final_list = ListNode()
        p2 = final_list


        # Stack to use keep track of reversed part of list
        stack = []
        counter = 1

        # Iterate through list
        while head:
            # If we meet left side, append to stack, then pop afterwards to reverse list
            if counter == left:
                while counter != right:
                    stack.append(head.val)
                    head = head.next
                    counter += 1
                stack.append(head.val)
                head = head.next
                counter += 1
                while len(stack) != 0:
                    p2.next = ListNode(stack.pop())
                    p2 = p2.next
            # Otherwise keep list moving
            else:
                p2.next = ListNode(head.val)
                head = head.next
                counter += 1
                p2 = p2.next

        return final_list.next
