class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        i = time // (n - 1)
        rem = time % (n - 1)
        if i % 2 == 1:
            return n - rem
        else:
            return 1 + rem
