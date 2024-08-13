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
