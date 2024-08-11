# DP
# Runtime: O(n)
# Space: O(1)

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2



# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         #edge case
#         if len(nums) <= 2:
#             return max(nums)
        
#         #dp
#         L = len(nums)
#         dp = [0 for i in range(L)]
#         dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        
#         for i in range(2, L):
#             dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
#         return dp[-1]
