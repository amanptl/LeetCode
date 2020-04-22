def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        count = 0
        total = 0
        d = defaultdict(int)
        d[0] = 1
        for i in range(len(nums)):
            total += nums[i]
            if (total-k) in d:
                count += d[total-k]
            d[total] += 1
        
        return count