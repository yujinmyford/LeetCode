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
