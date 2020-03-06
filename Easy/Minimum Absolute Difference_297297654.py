class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        curr_min = 255
        ans = []
        for i in range(0,len(arr)-1):
            if abs(arr[i]-arr[i+1]) < curr_min:
                curr_min = abs(arr[i]-arr[i+1])
        
        for i in range(0,len(arr)-1):
            if abs(arr[i]-arr[i+1]) == curr_min:
                ans.append([arr[i],arr[i+1]])
        
        return ans
