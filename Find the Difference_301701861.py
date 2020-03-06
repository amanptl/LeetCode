class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        v=[]
        for e in s:
            v.append(e)
        for e in t:
            if e in v:
                v.remove(e)
            else:
                v.append(e)
        return(v[0])
                
        
