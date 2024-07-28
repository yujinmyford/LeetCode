# Sliding Window
# Runtime: O(n)
# Space: O(n)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "":
            return ""
        
        countT = {}
        window = {}

        for char in t:
            countT[char] = 1 + countT.get(char, 0)
        
        have = 0
        need = len(countT)

        res = [-1, -1]
        resLen = float("infinity")
        left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = 1 + window.get(char, 0)

            if char in countT and window[char] == countT[char]:
                have += 1
            
            while have == need:
                # update result
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                # pop from left
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1

        left = res[0]
        right = res[1]

        if resLen == float("infinity"):
            return ""
        else:
            return s[left:right+1]
