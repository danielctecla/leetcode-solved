
class Solution:
    def platesBetweenCandles(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)

        # Prefix sum: count plates
        prefix = [0] * n
        for i in range(n):
            prefix[i] = (1 if s[i] == "*" else 0)
            if i > 0:
                prefix[i] += prefix[i - 1]

        # Closest candle to the left
        left_candle = [-1] * n
        last_candle = -1

        for i in range(n):
            if s[i] == "|":
                last_candle = i
            left_candle[i] = last_candle

        # Closest candle to the right
        right_candle = [-1] * n
        next_candle = -1

        for i in range(n - 1, -1, -1):
            if s[i] == "|":
                next_candle = i
            right_candle[i] = next_candle

        # Answer queries
        ans = []

        for left, right in queries:
            first = right_candle[left]
            last = left_candle[right]

            if first != -1 and last != -1 and first < last:
                ans.append(prefix[last] - prefix[first])
            else:
                ans.append(0)

        return ans
