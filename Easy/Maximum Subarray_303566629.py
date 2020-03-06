class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*(len(nums)+1)
        m = float('-inf')
        for i in range(1,len(dp)):
            dp[i] = max(dp[i-1]+nums[i-1],nums[i-1])
            if m<dp[i]:
                m=dp[i]
        
        return m
