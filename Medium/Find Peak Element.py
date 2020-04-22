def findPeakElement(self, nums: List[int]) -> int:
        def search(l,r):
            if l == r:
                return l
            mid = (l+r)//2
            if  nums[mid] > nums[mid+1]:
                return search(l,mid)
            return search(mid+1,r)
        
        return search(0,len(nums)-1)