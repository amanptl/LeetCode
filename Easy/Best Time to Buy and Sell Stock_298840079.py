class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        dp = [0] * (len(prices)+1)
        m = 0
        profit = 0
        
        for i in range(len(dp)-2,-1,-1):
            if prices[i] > m:
                m = prices[i]
            dp[i] = m
        
        for i in range(len(prices)):
            if dp[i+1] - prices[i] > profit:
                profit = dp[i+1] - prices[i]
        
        return profit
