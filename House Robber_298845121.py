class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        max_ = dp[0]
        for i in range(2,len(dp)):
            dp[i] = max_ + nums[i]
            max_ = max(max_, dp[i-1])
        return max(max_,dp[len(nums)-1])
