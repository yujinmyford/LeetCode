# Neetcode
# Stack, backtracking(recursion)


# Only add open parentheses if openN < n
# Only add a closing parentheses if closedN < openN
# return if openN == closedN == n
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            # pop because stack is global variable, not passing in individually
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
