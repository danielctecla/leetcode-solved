class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [-1]*(amount + 1)
        dp[0] = 0

        for i in range(1,amount + 1):
            for coin in coins:
                
                temp = i - coin
                if temp < 0 or dp[temp] == -1:
                    continue

                total = 1 + dp[temp]
                if dp[i] == -1 or total < dp[i]:
                    dp[i] = total
                    
        return dp[amount]
