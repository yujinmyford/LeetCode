# 2 Pointers
# Runtime: O(n)
# Space: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            if height[left] < height[right]:
                cur_area = height[left] * (right - left)
                max_area = max(max_area, cur_area)
                left += 1
            else:
                cur_area = height[right] * (right - left)
                max_area = max(max_area, cur_area)
                right -= 1
        return max_area

# # Neetcode

# # Brute Force, calculates every single combination possible
# # Time complexity = O(n^2)
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         res = 0

#         for l in range(len(hieght)):
#             for r in range(l + 1, len(height)):
#                 area = (r - l) * min(height[l], height[r])
#                 res = max(res, area)
#         return res

# # Two pointer
# # Time complexity = O(n)
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         l, r = 0, len(height) - 1
#         res = 0

#         while l < r:
#             res = max(res, min(height[l], height[r]) * (r - l))
#             # Move pointer for smaller side
#             if height[l] < height[r]:
#                 l += 1
#             elif height[r] <= height[l]:
#                 r -= 1
            
#         return res

