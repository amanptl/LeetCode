class Solution:
    def isHappy(self, n: int) -> bool:
        d=0
        s = 0
        h={}
        while s!=1:
            while n>0:
                d,n = n%10, n//10
                s+=d**2
            if(s==1):
                return True
            elif s in h:
                return False
            h[s]=""
            n,s=s,0
        return False
