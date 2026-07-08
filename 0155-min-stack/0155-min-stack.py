class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [2e31 - 1]

    def push(self, value: int) -> None:
        self.stack.append(value)
        self.minStack.append(min(self.minStack[-1], value))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()