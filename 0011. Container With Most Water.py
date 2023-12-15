# 2 Pointers
# Runtime: O(n)
# Space: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Instantiate left, right, and max_area
        left = 0
        right = len(height) - 1
        max_area = 0
    
        while left < right:
            # If left is smaller, use left to calculate the area since it is smaller, then update max_area and increment left
            if height[left] < height[right]:
                cur_area = height[left] * (right - left)
                max_area = max(max_area, cur_area)
                left += 1
            # If right is smaller, use right to calculate the area since it is smaller, then update max_area and decrement right
            else:
                cur_area = height[right] * (right - left)
                max_area = max(max_area, cur_area)
                right -= 1
        return max_area

