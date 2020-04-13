def findMaxLength(self, nums: List[int]) -> int:
        d = {}
        d[0] = -1
        m, count = 0, 0
        for i in range(len(nums)):
            count += 1 if nums[i] == 1 else -1
            if count in d:
                m = max(m, i - d[count])
            else:
                d[count] = i
        
        return m