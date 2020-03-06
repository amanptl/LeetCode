class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        e = []
        ans = []
        
        for i in range(len(S)):
            if(S[i] == C):
                e.append(i)
        
        for i in range(len(S)):
            ans.append(min(abs(i-ei) for ei in e))
        
        return ans
            
