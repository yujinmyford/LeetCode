class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s [i] != "]":
                stack.append(s[i])
            else:
                curSub = ""
                # pop all characters
                while stack[-1] != "[":
                    curSub = stack.pop() + curSub

                # to pop opening bracket
                stack.pop()

                k = ""

                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                stack.append(int(k) * curSub)


        return "".join(stack)
