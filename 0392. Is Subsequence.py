class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
    
        sPointer = 0
        tPointer = 0
        
        while sPointer < len(s) and tPointer < len(t):
            if s[sPointer] == t[tPointer]:
                sPointer += 1
            tPointer += 1
        
        if sPointer == len(s):
            return True
        return False
