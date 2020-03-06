class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.max_ = 0
        self.n = len(arr)
        def bm(s):
            i = 0
            for e in s:
                i += 2**(ord(e)-97)
            return i
        
        def mb(a,b):
            if (bm(a)&bm(b)) == 0:
                return True
            else:
                return False
            
            
        def backtrack(index,s):
            self.max_ = max(len(s), self.max_)
            if index == self.n:
                return
            for i in range(index, self.n):
                if len(arr[i]) > len(set(arr[i])):
                    continue
                if mb(s, arr[i]):
                    backtrack(i+1,s+arr[i])
                
        backtrack(0,"")
        return self.max_
        
        
    
    
