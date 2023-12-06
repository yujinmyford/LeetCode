# Stack
# Runtime: O(n)
# Space: O(n)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Stack to keep track of calculations
        stack = []

        # Iterate through tokens
        for token in tokens:
            # If token is +, pop the last two and add then append
            if token == "+":
                second = stack.pop()
                first = stack.pop()
                stack.append(first + second)
            # If token is -, subtract then append
            elif token == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
            # If token is *, multiply then append
            elif token == "*":
                second = stack.pop()
                first = stack.pop()
                stack.append(first * second)
            # If token is /, divide (with trunc, as specified) then append
            elif token == "/":
                second = stack.pop()
                first = stack.pop()
                stack.append(trunc(first / second))
            # Means token is a number, convert to integer then append to stack
            else:
                stack.append(int(token))

        # At the end of iterating through tokens, we'll have the final calculation in stack
        return int(stack[0])
