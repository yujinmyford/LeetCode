# Runtime: O(n)
# Space: O(n)

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums2 = [0] * (2 * len(nums))

        for i in range(2 * len(nums)):
            nums2[i] = nums[(i % len(nums))]
        
        return nums2
