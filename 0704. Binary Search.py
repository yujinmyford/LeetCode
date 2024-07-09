# Binary Search
# Runtime: O(log n)
# Space:

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            # (left + right) // 2 can lead to overflow
            mid = (right + left) // 2
            # If target is less than mid, means target is in left half 
            if nums[mid] > target:
                right = mid - 1
            # If target is greater than mid, means target is in right half
            elif nums[mid] < target:
                left = mid + 1
            # Else, means mid is the target, return mid
            else:
                return mid
        # If we make it out without returning means it's not in the list
        return -1


# # Neetcode
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l, r = 0, len(nums) - 1

#         while l <= r:
#             m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
#             if nums[m] > target:
#                 r = m - 1
#             elif nums[m] < target:
#                 l = m + 1
#             else:
#                 return m
#         return -1
