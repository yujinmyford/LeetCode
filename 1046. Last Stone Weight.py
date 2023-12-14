# Heap
# Runtime: O(n^2)
# Space: O(1)

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        # Invert stone values to simulate max-heap
        for stone in stones:
            heapq.heappush(pq, -stone)

        # While max-heap
        while pq:
            # Pop largest, and invert back to original value
            stone1 = -heapq.heappop(pq)
            # This means stone1 is the only remaining stone, so return                  stone1
            if not pq:
                return stone1
            # Pop second largest, and also invert back to original value
            stone2 = -heapq.heappop(pq)
            # If stones aren't equal, put remainder of smashed back into heap, if they are equal no need to push anything since they are both smashed
            if stone1 > stone2:
                heapq.heappush(pq, -(stone1 - stone2))

       # Means we made it out of while loop, meaning there are no stones remaining
        return 0
