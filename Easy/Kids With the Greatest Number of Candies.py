def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        
        m = max(candies)
        
        for candy in candies:
            if candy + extraCandies >= m:
                res.append(True)
            else:
                res.append(False)
        
        return res