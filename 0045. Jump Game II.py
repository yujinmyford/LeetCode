# Greedy

class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0
        while r < (len(nums) - 1):
            maxJump = 0
            for i in range(l, r + 1):
                maxJump = max(maxJump, i + nums[i])
            l = r + 1
            r = maxJump
            res += 1
        return res



# DP Solution

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0  # No jumps needed if there's one or no element

        dp = [float('inf')] * n  # Initialize dp array
        dp[0] = 0  # No jumps needed to reach the first index

        for i in range(n):
            for j in range(1, nums[i] + 1):
                if i + j < n:  # Ensure we don't go out of bounds
                    dp[i + j] = min(dp[i + j], dp[i] + 1)

        return dp[-1]  # The last index will have the minimum jumps
