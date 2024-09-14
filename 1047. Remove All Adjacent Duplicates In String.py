class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = []
        
        for char in s:
            if len(stack) > 0 and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
                
                
        res = ""
        
        for char in stack:
            res += char
        
        return res
