class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #d=collections.defaultdict(int)
        n = len(nums)+1
        d = {i for i in nums}
        #for i in nums:
        #    d[i] = ""
        for i in range(n):
            if i not in d:
                return i
