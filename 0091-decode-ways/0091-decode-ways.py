class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        n = len(s)
        dp = [0]*n
        dp[0] = 1
        dp[-1] = 1
        
        for i in range(1,n):
            doubleNum = int(s[i-1:i+1])

            if doubleNum == 0:
                return 0
            if (doubleNum % 10) == 0 and doubleNum not in [10,20]:
                return 0

            if s[i] == "0":
                dp[i] = dp[i - 2]
            elif doubleNum > 26 or s[i - 1] == "0":
                dp[i] = dp[i - 1]
            else:
                dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[-1]
            
                