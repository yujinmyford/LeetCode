# Stack, Hashmap
# Runtime: O(n)
# Space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        # Hashmap to keep track of open and close brackets
        match = {"(": ")", "{": "}", "[": "]"}
        # Stack to use
        stack = []

        # Iterate through s
        for cur in s:

            # Edge case where there is only closing bracket
            # Stack is empty and adding closing bracket
            if not stack and cur not in match:
                return False
            # If cur is in match, means opening bracket, append to stack then continue
            if cur in match:
                stack.append(cur)
                continue
            # If cur matches opening bracket of top of stack, valid bracket. Pop then continue
            if match[stack[-1]] == cur:
                stack.pop()
                continue
            # If cur does not correspond to opening bracket, invalid parentheses
            else:
                return False
        
        # After iterating through stack, if stack is empy, return true. If not, false
        if not stack:
            return True
        else:
            return False



# # 7/28/2024
# # Runtime: O(n)
# # Space: O(n)
# class Solution:
#     def isValid(self, s: str) -> bool:
        
#         hashmap = {')': '(', '}': '{', ']': '['}
#         stack = []

#         for paren in s:
#             if paren not in hashmap:
#                 stack.append(paren)
#             else:
#                 if len(stack) == 0 or hashmap[paren] != stack.pop():
#                     return False
        
#         if len(stack) == 0:
#             return True
#         else:
#             return False
