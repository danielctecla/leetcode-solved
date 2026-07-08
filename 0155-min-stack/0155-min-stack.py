class MinStack:

    def __init__(self):
        self.stack = []
        self.minValue = 2e31 - 1

    def push(self, value: int) -> None:
        self.stack.append(value)
        if value < self.minValue:
            self.minValue = value

    def pop(self) -> None:
        last = self.stack.pop()
        if last == self.minValue:
            self.minValue = 2e31 - 1
            for element in self.stack:
                self.minValue = min(self.minValue, element)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minValue

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()