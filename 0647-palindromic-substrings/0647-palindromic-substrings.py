class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        totalPalindromic = n

        for size in range(n):
            for i in range(n - size):
                j = i + size
                if size == 0:
                    dp[i][i] = True
                elif size == 1:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        totalPalindromic += 1    
                else: 
                    if s[i] == s[j] and dp[i + 1][j - 1]:
                        dp[i][j] = True
                        totalPalindromic += 1
        

        return totalPalindromic