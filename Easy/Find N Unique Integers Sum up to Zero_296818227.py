class Solution:
    def sumZero(self, n: int) -> List[int]:
        import numpy as np
        ans = np.zeros(n)
        if n%2 !=0:
            for i in range(1, int(n/2)+1):
                ans[i] = int(i+1)
                ans[-i] = int(-i-1)
        else:
            for i in range(int(n/2)):
                ans[i] = int(i+1)
                ans[-i-1] = int(-i-1)
        print(sum(ans))
        return ans
                
            
