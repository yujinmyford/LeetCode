# Runtime: O(N)
# Space: O(N)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Create set, and initialize left pointer and longest variable to return
        stringSet = set()
        left = 0
        longest = 0

        # Iterate through list, and move pointers accordingly
        for right in range(len(s)):
            while s[right] in stringSet:
                stringSet.remove(s[left])
                left += 1
            stringSet.add(s[right])
            longest = max(longest, right - left + 1)

        return longest
