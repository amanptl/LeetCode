class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, x in enumerate(nums):
            n = target - x
            if n not in d:
                d[x] = i
            else:
                return [d[n], i]
        
        
        
