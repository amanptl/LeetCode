class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        d={}
        n = len(nums)+1
        for i in nums:
            d[i] = ""
        for i in range(n):
            if i not in d:
                return i
