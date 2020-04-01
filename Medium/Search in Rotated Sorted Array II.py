def search(self, nums: List[int], target: int) -> bool:
        def rotatedSearch(a,lo,hi,x):
            if hi < lo:
                return False
            mid = int((hi+lo)/2)
            if a[mid] == x:
                return True
            if a[lo] < a[mid]:
                if x>=a[lo] and x<a[mid]:
                    return rotatedSearch(a,lo,mid-1,x)
                else:
                    return rotatedSearch(a,mid+1,hi,x)
            elif a[mid] < a[lo]:
                if x>a[mid] and x<=a[hi]:
                    return rotatedSearch(a,mid+1,hi,x)
                else:
                    return rotatedSearch(a,lo,mid-1,x)
            elif a[lo] == a[mid]:
                if a[mid]!=a[hi]:
                    return rotatedSearch(a,mid+1,hi,x)
                else:
                    result = rotatedSearch(a,lo,mid-1,x)
                    if result == False:
                        return rotatedSearch(a,mid+1,hi,x)
                    else:
                        return result
            return False
        
        left = 0
        right = len(nums)-1
        return rotatedSearch(nums,left,right,target)