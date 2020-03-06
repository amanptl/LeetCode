class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        t,p = 0,0
        for i in reversed(s):
            if d[i] >= p:
                t += d[i]
            else:
                t-=d[i]
            p = d[i]
        return t
