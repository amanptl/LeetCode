class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(int(len(nums)/2)):
            a,b = nums[2*i],nums[2*i+1]
            for j in range(a):
                ans.append(b)
        return ans
            
