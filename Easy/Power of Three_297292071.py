class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        import math
        if n<1:
            return False
        x = (math.log10(n)/math.log10(3))
        if(x % 1==0):
            return True
        return False
