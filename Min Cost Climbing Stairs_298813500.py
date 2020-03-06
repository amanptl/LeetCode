class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #dp = [0]*len(cost)
        dp0,dp1 = cost[0],cost[1]
        for i in range(2,len(cost)):
            temp = min(dp0,dp1)+cost[i]
            dp0 = dp1
            dp1 = temp
        return min(dp0,dp1)
        
