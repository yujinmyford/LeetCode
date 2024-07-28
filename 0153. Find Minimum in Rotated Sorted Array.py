# Binary Search
# Runtime: O(log n)
# Space: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1
        smallest = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                smallest = min(smallest, nums[left])
                break
            
            mid = (right + left) // 2
            smallest = min(smallest, nums[mid])

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        
        return smallest
