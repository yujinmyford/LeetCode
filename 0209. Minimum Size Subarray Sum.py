# Two Pointer
# Runtime: O(n)
# Space: O(1)

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        right = 0
        curSum = 0
        shortest = float('inf')

        while right < len(nums):
            curSum += nums[right]
            while left < len(nums) and curSum >= target:
                shortest = min(shortest, right - left + 1)
                curSum -= nums[left]
                left += 1
            right += 1
        
        if shortest == float('inf'):
            return 0
        else:
            return shortest
