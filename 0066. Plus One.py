# Runtime: O(n)
# Space: O(1)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        curSum = 0
        
        while i >= 0:
            curSum = digits[i] + 1
            digits[i] = curSum % 10
            if curSum >= 10:
                i -= 1
            else:
                break
        
        if curSum == 10:
            digits.insert(0, 1)
        
        return digits
