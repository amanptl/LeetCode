def brokenCalc(self, X: int, Y: int) -> int:
        ans = 0
        while Y > X:
            ans += 1
            if Y%2 == 0:
                Y = Y // 2
            else:
                Y += 1
        
        return ans + X-Y