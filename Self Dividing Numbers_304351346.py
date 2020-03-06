class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def checker(n):
            n_ = n
            d =-1
            while n_>0:
                d = n_%10
                n_ = n_//10
                if d==0 or n%d != 0:
                    return False
            return True
        a = []
        for i in range(left,right+1):
            if checker(i):
                a.append(i)
        return a
