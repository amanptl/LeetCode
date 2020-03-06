class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a = set()
        nums.sort()
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            t = -1*nums[i]
            while l<r:
                if nums[l]+nums[r] == t:
                    a.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l]+nums[r]<t:
                    l+=1
                else:
                    r-=1
        return list(a)
