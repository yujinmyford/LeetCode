# Dynamic Programming, hashmap
# Runtime: O(n)
# Space: O(1)
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        return self._dp_helper(s, dp)
    
    def _dp_helper(self, data, dp):
        # Base Case 1: Empty string
        if not data:
            return 1

        first_call, second_call = 0, 0

        # check in hashmap, memoization
        if data in dp: 
            return dp[data]

        # check for 1 digit
        if 1 <= int(data[0]) <= 9:
            first_call = self._dp_helper(data[1:], dp)
        
        # check for 2 digit
        if len(data) > 1:
            temp = data[0] + data[1]
        else:
            temp = data[0]
        if 10 <= int(temp) <= 26:
            second_call = self._dp_helper(data[2:], dp)

        dp[data] = first_call + second_call
        return dp[data]



# # Dynamic Programming solution
# # Runtime: O(n)
# # Space: O(1)

# class Solution:
#     def numDecodings(self, s: str) -> int:
#         dp = {len(s): 1}
#         for i in range(len(s) - 1, -1, -1):
#             if s[i] == "0":
#                 dp[i] = 0
#             else:
#                 dp[i] = dp[i + 1]

#             if i + 1 < len(s) and (
#                 s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
#             ):
#                 dp[i] += dp[i + 2]
#         return dp[0]

# # Memoization solution 
# # Runtime: O(n)
# # Space: O(n)

# class Solution:
#     def numDecodings(self, s: str) -> int:
#         dp = {len(s): 1}

#         def dfs(i):
#             # Already cached
#             if i in dp:
#                 return dp[i]
#             # Bad case, can't start with 0
#             if s[i] == "0":
#                 return 0


#             res = dfs(i + 1)
#             if i + 1 < len(s) and (
#                 s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
#             ):
#                 res += dfs(i + 2)
#             dp[i] = res
#             return res

#         return dfs(0)
