class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        min_value = 0
        if self.stack:
            min_value = min(value, self.stack[-1][1])
        else:
            min_value = min_value = value

        self.stack.append((value,min_value))
        
    
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        value, _ = self.stack[-1]
        return value
    
    def getMin(self) -> int:
        _, min_value = self.stack[-1]
        return min_value