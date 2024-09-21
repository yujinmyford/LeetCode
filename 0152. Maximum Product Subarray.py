class Solution:
    def maxProduct(self, nums):
        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max(max_so_far * curr, min_so_far * curr))
            min_so_far = min(curr, min(max_so_far * curr, min_so_far * curr))

            # Update max_so_far after updates to min_so_far to avoid overwriting it
            max_so_far = temp_max
            # Update the result with the maximum product found so far
            result = max(max_so_far, result)

        return result

# DP
# Runtime: O(n)
# Space: O(1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        # Keep curMin to keep track of negative values
        curMin, curMax = 1, 1

        for n in nums:
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res
