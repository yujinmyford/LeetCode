# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Heap, Linked List
# Runtime: n log k, where n is the total number of nodes across all lists and k is the number of linked lists
# Space: O(n)

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        # shortcut, just return 1st linkedlist if only a single list
        if len(lists) == 1:
            return lists[0]

        # create a temporary head and a node pointer to track what
        #     elements we've added to the return list
        head = ListNode(None)
        cur = head

        # Create a min-heap tracking the smallest elements seen so far
        #   (up to k elements adde)
        pq = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(pq, (lists[i].val, i))
                lists[i] = lists[i].next

        
        # while there's elts in the queue, 
        #   pop its minimum element and add it to the return llist
        #   if it has a next element, add that to the priority queue in its place
        while pq:
            # value, next_node = heapq.heappop(pq)
            # node.next = next_node
            # if next_node.next:
            #     heapq.heappush(pq, (next_node.next.val, next_node.next))
            # node = node.next
            val, i = heapq.heappop(pq)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[i]:
                heapq.heappush(pq, (lists[i].val, i))
                lists[i] = lists[i].next
        
        return head.next
