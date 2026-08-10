class Solution:

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        maxLength = 1
        index = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for L in range(1,n + 1):
            for i in range(0,n - L + 1):
                if L == 1:
                    dp[i][i] = True
                    continue
                elif L == 2:
                    dp[i][i + L - 1] = True if s[i] == s[i + L - 1] else False
                else:
                    
                    dp[i][i + L - 1] = True if s[i] == s[i + L - 1] and dp[i + 1][i + L - 1 - 1] else False
                
                if dp[i][i + L - 1] == True:
                    maxLength = L
                    index = i

        return s[index:index + maxLength]