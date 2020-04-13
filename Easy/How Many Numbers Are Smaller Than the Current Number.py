def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
        d = defaultdict(int)
        res = []
        for num in nums:
            d[num] += 1
        
        for num in nums:
            count = 0
            for i in d:
                if i < num:
                    count += d[i]
                
            res.append(count)
        return res