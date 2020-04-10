def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = 0
        for trip in trips:
            n = max(n, trip[2])
        
        route = [0] * (n+1)
        
        for load, s, e in trips:
            route[s] += load
            route[e] -= load
        
        for curr in route:
            capacity -= curr
            if capacity < 0:
                return False
        return True