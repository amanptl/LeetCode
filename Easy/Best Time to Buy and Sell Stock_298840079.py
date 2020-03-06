class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minStock = float('inf')
        
        for stock in prices:
            if stock < minStock:
                minStock = stock
            else:
                maxProfit = max(maxProfit, stock - minStock)
        return maxProfit
