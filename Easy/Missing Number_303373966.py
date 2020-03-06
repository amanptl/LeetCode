class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s1 = 0
        for i in range(0,len(nums)+1):
            s1+=i
        s2 = 0
        for i in nums:
            s2+=i
        return s1-s2
