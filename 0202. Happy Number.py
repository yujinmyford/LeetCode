# Array
# Runtime: O(n)
# Space: O(n)

class Solution:
    def isHappy(self, n: int) -> bool:
        computed = set()

        # Keep loop going until we detect cycle or find it is happy number
        while (n != 1):
            cur = 0
            # calculate for each digit squared
            while (n > 0):
                i = n % 10
                cur += i * i
                n = n // 10

            # If cur is in computed, return false since that means cycle
            if cur in computed:
                return False
            # If not add it to computed
            else:
                computed.add(cur

            # Update n to be cur
            n = cur

        # If we make it out of the while loop, it means n == 1, meaning it is a happy number
        return True

