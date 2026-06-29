class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = []
        
        for i in range(len(temperatures) - 1, -1, -1):
            count = 1
            
            while stack:
                temp = stack[-1]
                if temperatures[i] >= temp[0]:
                    stack.pop()
                    count += temp[1]
                else:
                    stack.append((temperatures[i],count))
                    answer.append(count)
                    break

            if not stack:
                stack.append((temperatures[i],0))
                answer.append(0)

        return answer[::-1]