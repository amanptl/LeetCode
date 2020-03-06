class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        import numpy as np
        dist = []
        for (x,y) in points:
            dist.append(np.sqrt(abs((x**2)+(y**2))))
        print(dist)
        print(points)
        ans = [x for y,x in sorted(zip(dist,points))]
        
        return ans[:K]
