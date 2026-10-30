class Solution:
    def platesBetweenCandles(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        prefix = [0] * n
        prefix[0] = 1 if prefix[0] == "*" else 0
        
        for i in range(1,n):
            if s[i] == "*":
                prefix[i] = 1
            prefix[i] += prefix[i - 1]
        
        last_candle = -1
        left_candle = [0] * n
        for i in range(n):
            if s[i] == "|":
                last_candle = i
            left_candle[i] = last_candle
        
        next_candle = -1
        right_candle = [0] * n
        for i in range(n-1,-1,-1):
            if s[i] == "|":
                next_candle = i
            right_candle[i] = next_candle

        ans = []
        for left, right in queries:
            
            rt = left_candle[right]
            lt = right_candle[left]

            if rt != lt and lt <= right and rt >= left:
                ans.append(prefix[rt] - prefix[lt])
            else:
                ans.append(0)

        return ans