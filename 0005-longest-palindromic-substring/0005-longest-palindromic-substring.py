class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        maxLength = 1
        index = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for L in range(1, n + 1):
            for i in range(n - L + 1):
                j = i + L - 1

                if L == 1:
                    dp[i][j] = True
                elif L == 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

                if dp[i][j]:
                    maxLength = L
                    index = i

        return s[index:index + maxLength]