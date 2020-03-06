class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)
        
        for i in range(l):
            if nums[i] < 1 :
                nums[i] = l+1
        
        for i in range(l):
            if abs(nums[i]) <= l: 
                nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])
        
        for i in range(l):
            if nums[i] > 0:
                return i+1
        return l+1
