class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        listS = list(s)
        listT = list(t)
        if len(listS) != len(listT):
            return False

        for i, c in enumerate(listS):
            for j, ch in enumerate(listT):
                if c == ch:
                    del(listT[j])
                    break
        
        if len(listT) == 0:
            return True
        return False
