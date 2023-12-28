# Stack
# Runtime: O(1) for all functions 

class minStack:
    # Stack is for actual stack, prevMins is used to keep track of previous minimums
    def __init__(self):
        self.stack = []
        self.currentMin = float('inf')
        self.prevMins = []

    # Start by pushing val to the stack
    def push(self, val: int) -> None:
        self.stack.append(val)
        # If the value we're pushing is less than currentMin, append currentMin to prevMins and update currentMin
        if val <= self.currentMin:
            self.prevMins.append(self.currentMin)
            self.currentMin = val

    def pop(self) -> None:
        # If the last element in stack is currentMin, update currentMin to be the last element from prevMin
        if self.stack[-1] == self.currentMin:
            self.currentMin = self.prevMins.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.currentMin

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
