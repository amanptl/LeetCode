class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l = []
        nums.sort()
        for n in nums:
            if n not in l:
                l.append(n)
            else:
                l.pop()
        return l.pop()
