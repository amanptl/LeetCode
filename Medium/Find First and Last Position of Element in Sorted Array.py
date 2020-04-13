def searchRange(self, nums: List[int], target: int) -> List[int]:
        def foo(left):
            lo = 0
            hi = len(nums)
            
            while lo < hi:
                mid = (lo+hi)//2
                if nums[mid] > target or (left and target == nums[mid]):
                    hi = mid
                else:
                    lo = mid+1
            
            return lo
        
        l = foo(True)
        if l == len(nums) or nums[l] != target:
            return [-1, -1]
        return [l, foo(False)-1]