# Runtime: O(n)
# Space: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        
        return l


# # 7/14/2024:

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         l = 1

#         for r in range(1, len(nums)):
#             if nums[r] != nums[r - 1]:
#                 nums[l] = nums[r]
#                 l += 1
        
#         return l
