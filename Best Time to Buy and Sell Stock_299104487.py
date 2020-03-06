class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 or len(prices) == 1:
            return 0
        max_ = max(prices)
        dp = [0]*len(prices)
        max_p = 0
        for i in range(len(prices)-1):
            if prices[i]==max_:
                max_ = max(prices[i+1:])
                continue
            temp = max_ - prices[i]
            if temp > max_p:
                max_p = temp
        return max_p
