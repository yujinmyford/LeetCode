# Runtime: O(n)
# Space: O(1)

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Start by sorting nums
        nums.sort()
        closDiff = 10 ** 5
        closest = 10 ** 5
        for i in range(len(nums)):
            # Set left and right pointers
            left = i + 1
            right = len(nums) - 1

            # Move pointers accordingly
            while left < right:
                curSum = nums[i] + nums[left] + nums[right]
                if abs(target - curSum) < closDiff:
                    closest = curSum
                    closDiff = abs(target - curSum)

                if curSum < target:
                    left += 1
                elif curSum > target:
                    right -= 1
                else:
                    return target
        
        return closest

