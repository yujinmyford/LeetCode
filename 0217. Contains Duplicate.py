class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        containsList = set()
        
        for i, num in enumerate(nums):
            if num in containsList:
                return True
            containsList.add(num)
        
        return False




# # 7/25
# # Runtime: O(n)
# # Space: O(n)
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:

#         exists = {}

#         for i in nums:
#             if i in exists:
#                 return True
#             else:
#                 exists[i] = 1
        

#         return False
