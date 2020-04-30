def maxProduct(self, nums: List[int]) -> int:
        loMin = loMax = glMax = nums[0]
        
        for i in range(1,len(nums)):
            t = loMin
            loMin = min(loMin*nums[i],nums[i],loMax*nums[i])
            loMax = max(t*nums[i],nums[i],loMax*nums[i])
            glMax = max(loMax,glMax)
        
        return glMax