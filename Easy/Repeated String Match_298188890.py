class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        for b in B:
            if b not in A:
                return -1
        A_temp=""
        for i in range(1,len(B)+1):
            A_temp+=A
            if (A_temp).find(B) != -1:
                return i
            if len(A_temp)>len(A+B):
                return -1
        
