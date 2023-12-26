# List
# Runtime: O(n)
# Space: O(1)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Instantiate max_jump, which keeps track of the max spot we can jump to
        max_jump = 0
        for i in range(len(nums)):
            # Break early, if we either reach a point max_jump can't reach, or if max_jump is already able to reach the end
            if i > max_jump or max_jump >= lens(nums) - 1:
                break
            # Update max_jump if needed
            max_jump = max(max_jump, i + nums[i])
        # Will return True if we can jump to the end, False if not
        return max_jump >= len(nums) - 1
