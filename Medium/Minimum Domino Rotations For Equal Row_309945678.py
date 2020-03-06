class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        def check(v):
            a = 0
            b = 0
            for i in range(n):
                if A[i]!=v and B[i]!=v:
                    return -1
                elif A[i]!=v:
                    a+=1
                elif B[i]!=v:
                    b+=1
            return min(a,b)
        
        r = check(A[0])
        if A[0] == B[0] or r != -1:
            return r
        else:
            return check(B[0])
        
        
        
        
            
