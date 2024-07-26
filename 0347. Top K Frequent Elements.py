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



# # 7/25:
# # Heap & Hashmap
# # Runtime: O(k logn)
# # Space: O(n)
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
#         frequency = {}

#         for num in nums:
#             if num not in frequency:
#                 frequency[num] = 1
#             else:
#                 frequency[num] += 1
        
#         min_heap = []

#         for key in frequency:
#             if len(min_heap) < k:
#                 heapq.heappush(min_heap, (frequency[key], key))
#             else:
#                 heapq.heappush(min_heap, (frequency[key], key))
#                 heapq.heappop(min_heap)
        

#         most_freq = []

#         for pair in min_heap:
#             most_freq.append(pair[1])
        
#         return most_freq


# # Runtime: O(n)

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = {}
#         freq = [[] for i in range(len(nums) + 1)]

#         for n in nums:
#             count[n] = 1 + count.get(n, 0)
#         for n, c in count.items():
#             freq[c].append(n)

#         res = []
#         for i in range(len(freq) - 1, 0, -1):
#             for n in freq[i]:
#                 res.append(n)
#                 if len(res) == k:
#                     return res
