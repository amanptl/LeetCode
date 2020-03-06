class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        d=set(nums)
        n = len(nums)+1
        
        for i in range(n):
            if i not in d:
                return i
