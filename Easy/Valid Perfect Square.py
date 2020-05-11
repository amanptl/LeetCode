def isPerfectSquare(self, num: int) -> bool:
        if num == 0:
            return False
        if num == 1:
            return True
        lo = 0
        hi = num - 1
        
        while lo < hi:
            mid = (lo + hi) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                lo = mid + 1
            else:
                hi = mid
        
        return False