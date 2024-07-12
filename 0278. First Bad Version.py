# Runtime: O(log n)
# Space: O(1)
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            version = left + (right - left) // 2 
            if isBadVersion(version):
                right = version
            else:
                left = version + 1
        return left
