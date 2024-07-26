

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         finalArray = []
#         for i, x in enumerate(nums):
#             for j, y in enumerate(nums):
#                 if (i == j): break
#                 if (x + y == target):
#                     finalArray.append(j)
#                     finalArray.append(i)
#                     return finalArray

# 7/16
# Runtime: O(n)
# Space: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash = {}
        for i in range(len(nums)):
            nums_hash[nums[i]] = i
        
        cur_tar = 0
        for i in range(len(nums)):
            cur_tar = target - nums[i]
            if (cur_tar in nums_hash) and (nums_hash[cur_tar] != i):
                return [i, nums_hash[cur_tar]]




# # 7/25
# # Hashmap
# # Runtime: O(n)
# # Space: O(n)

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:

#         diff = {}
        
#         for i, num in enumerate(nums):
#             if num in diff:
#                 return [diff[num], i]
#             else:
#                 diff[target - num] = i


