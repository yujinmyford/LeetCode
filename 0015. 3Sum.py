# Two Pointers
# Runtime: O(N^2)
# Space: O(N)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(len(nums)):

            # Skip if previous number is same, to watch out for duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Initiate pointers
            left = i + 1
            right = len(nums) - 1

            while left < right:
                curSum = nums[i] + nums[left] + nums[right]

                # Move pointers accordingly
                if curSum > 0:
                    right -= 1
                elif curSum < 0:
                    left += 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
            
        return triplets


# # 7/27

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
        
#         triplets = []
#         nums.sort()

#         for i in range(len(nums)):

#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
            
#             l = i + 1
#             r = len(nums) - 1

#             while l < r:
#                 curSum = nums[i] + nums[l] + nums[r]

#                 if curSum > 0:
#                     r -= 1
#                 elif curSum < 0:
#                     l += 1
#                 else:
#                     triplets.append([nums[i], nums[l], nums[r]])
#                     l += 1
#                     r -= 1
#                     while nums[l] == nums[l - 1] and l < r:
#                         l += 1

#         return triplets
