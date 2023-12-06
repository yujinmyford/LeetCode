# Heap
# Runtime: O(k logn), where n is the number of elements we add, and k is the size of the heap
# Space: O(n), for the pq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency = {}

        # Hashmap called frequency, with the value as the key and the number of occurrences as the value
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1

        pq = []

        # Keep min-heap, based off number of occurrences
        for val in frequency:
            heapq.heappush(pq, (frequency[val], val))
            # If pq has more elements than k heappop to maintain size
            if len(pq) > k:
                heapq.heappop(pq)
        
        to_return = []
        # Then populate the to_return list with the values
        for val in pq:
            to_return.append(val[1])

        return to_return
