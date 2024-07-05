# Runtime: O(log n)
# Space: O(1)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        leftMost = self.binarySearch(nums, target, True)
        rightMost = self.binarySearch(nums, target, False)
        return [leftMost, rightMost]

    def binarySearch(self, nums, target, findLeftMost):
        left = 0
        right = len(nums) - 1
        idx = -1

        # Classic binary search
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                idx = mid
                # Modified to find left most and right most of target
                if findLeftMost:
                    right = mid - 1
                else:
                    left = mid + 1

        return idx
