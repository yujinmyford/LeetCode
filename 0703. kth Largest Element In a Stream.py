# Min Heap
# Runtime: O(n log k), where n is the number of elements we add, k is the size of the heap
# Space: O(n), since we add/delete elements while updating pq

import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # heappush value
        heapq.heappush(self.pq, val)
        # Ensure heap size is k. If heap size is larger than k after adding, pop smallest element
        if len(self.pq) > self.k:
            heapq.heappop(self.pq)
        return self.pq[0]
