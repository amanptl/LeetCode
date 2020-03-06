class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        import collections
        d = collections.defaultdict(int)
        ans=[]
        for i in nums:
            d[i]+=1
        for i in d:
            if d[i]==2:
                ans.append(i)
        return ans
        
