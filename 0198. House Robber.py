# Dynamic Programming
# Runtime: O(n)
# Space: O(n)

class Solution:
    def rob(self, nums: List[int]) -> int:
        # If there are only 1 or 2 elements in nums, we can just return the largest number
        if len(nums) <= 2:
            return max(nums)

        # Initialize nums[1]
        nums[1] = max(nums[0], nums[1])

        # DP subproblem, nums[i] = max(nums[i-2] + nums[i], nums[i-1])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i-2] + nums[i], nums[i-1])

        return nums[-1]
