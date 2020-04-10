def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        if len(nums) == 1:
            return True
        
        from collections import defaultdict
        d = defaultdict(int)
        nums.sort()
        for num in nums:
            d[num] += 1
        
        for num in nums:
            occ = d[num]
            if occ == 0:
                continue
            
            for i in range(k):
                if d[num+i] < occ:
                    return False
                d[num+i] = d[num+i] - occ
        return True