# Runtime: O(n)
# Space: O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one


# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 3:
#             return n
#         n1, n2 = 2, 3

#         for i in range(4, n + 1):
#             temp = n1 + n2
#             n1 = n2
#             n2 = temp
#         return n2
