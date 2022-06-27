class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        finalArray = []
        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                if (i == j): break
                if (x + y == target):
                    finalArray.append(j)
                    finalArray.append(i)
                    return finalArray
        
                