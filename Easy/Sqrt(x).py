def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        if x == 2:
            return 1
        
        lo = 0
        hi = x - 1
        
        while lo <= hi:
            mid = (lo+hi)//2
            curr = mid * mid
            if curr == x:
                return mid
            elif curr > x:
                hi = mid - 1
            else:
                lo = mid + 1
        
        if hi * hi <= x:
            return hi
        return lo