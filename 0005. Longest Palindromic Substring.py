# Runtime: O(N^2)
# Space: O(N) 

class Solution:
    def longestPalindrome(self, s: str) -> str:
        p_sub = ""
        p_sub_len = 0

        for i in range(len(s)):
            # odd, where pointers both point at i
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > p_sub_len:
                    p_sub = s[left:right+1]
                    p_sub_len = right - left + 1
                left -= 1
                right += 1
            

            # even, where left pointer is at i, right pointer is at i+1
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > p_sub_len:
                    p_sub = s[left:right+1]
                    p_sub_len = right - left + 1
                left -= 1
                right += 1

        
        return p_sub
