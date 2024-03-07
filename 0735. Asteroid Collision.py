# Runtime: O(N)
# Space: O(N)

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            # while stack is not empty, top of stack is positive, and asteroid is negative
            while stack and stack[-1] > 0 and asteroid < 0:
                # If top of stack is less than current asteroid, pop stack
                if stack[-1] + asteroid < 0:
                    stack.pop()
                # If top of stack is greater than asteroid break
                elif stack[-1] + asteroid > 0:
                    break
                # If top of stack and asteroid are equal, pop and break
                else:
                    stack.pop()
                    break
            else:
                stack.append(asteroid)
        
        return stack
