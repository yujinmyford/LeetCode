class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        containsList = set()
        
        for i, num in enumerate(nums):
            if num in containsList:
                return True
            containsList.add(num)
        
        return False
