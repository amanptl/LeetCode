def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        n = 0
        i = 0
        
        for d in reversed(A):
            n += d * (10**i)
            i += 1
        
        n += K
        res = []
        
        if n == 0:
            return [0]
        
        while n > 0:
            res.append(n%10)
            n = n//10
        
        return reversed(res)