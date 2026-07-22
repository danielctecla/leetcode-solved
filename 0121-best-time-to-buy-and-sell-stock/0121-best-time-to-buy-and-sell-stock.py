class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        left = 0
        right = 1
        
        while right < len(prices):
            profit = prices[right] - prices[left] 
            ans =  profit if profit > ans else ans
            if prices[right] < prices[left]:
                left = right
            right += 1

        return ans         