class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = set(nums)
        a = {}
        for i in s:
            a[nums.count(i)] = i
        return a[max(a)]
        
