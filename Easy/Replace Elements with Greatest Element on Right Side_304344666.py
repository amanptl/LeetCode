class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = max(arr)
        for i in range(len(arr)):
            if i == len(arr)-1:
                arr[i]=-1
                break
            if m == arr[i]:
                m = max(arr[i+1:])
            arr[i] = m
        return arr
            
