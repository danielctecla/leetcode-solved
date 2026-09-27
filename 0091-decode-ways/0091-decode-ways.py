class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        dp = (len(s) + 1) * [0]
        dp[0] = 1
        dp[1] = 1

        for i in range(1, len(s)):
            num = int(s[i - 1:i + 1])

            if s[i] != "0":
                dp[i + 1] += dp[i]

            if 10 <= num <= 26:
                dp[i + 1] += dp[i - 1]

        return dp[-1]





        
            
                