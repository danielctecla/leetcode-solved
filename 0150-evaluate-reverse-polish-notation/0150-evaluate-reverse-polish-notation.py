class Solution:
    def applyOperation(self, operator: str, val2: int, val1: int) -> int:
        print(f'{val1}{operator}{val2}')
        if operator == '+':
            return val1 + val2
        elif operator == '-':
            return val1 - val2
        elif operator == '*':
            return val1 * val2
        else:
            return int(val1 / val2)
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tkn in tokens:
            if tkn in ['+','-','*','/']:
                result = self.applyOperation(tkn,stack.pop(),stack.pop())
                stack.append(result)
            else:
                stack.append(int(tkn))

        return stack.pop()