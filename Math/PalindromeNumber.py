class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = str(x)
        a = []
        for i in range(len(y)):
            a.append(y[-(i+1)])
        string = [str(z) for z in a]
        finalString = ("".join(string))
        if (y == finalString):
            return True
        else:
            return False
