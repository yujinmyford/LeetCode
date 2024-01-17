# Runtime: O(n)
# Space: O(1), because output array does not count as extra space

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        # Calculate prefix
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]

        postfix = 1
        # Calculate postfix and put result in output array 
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
