class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def bt(f=0, c = []):
            if len(c) == k:
                o.append(c[:])
            for i in range(f,n):
                c.append(nums[i])
                bt(i+1, c)
                c.pop()
        o = []
        n = len(nums)
        for k in range(n+1):
            bt()
        return o
            
            
