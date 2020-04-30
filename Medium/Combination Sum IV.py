def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target + 1)]
        
        for i in range(1, len(dp)):
            total = 0
            for num in nums:
                if num < i and num > -1:
                    total += dp[i - num]
                elif num == i:
                    total += 1
            dp[i] = total
        return dp[-1]