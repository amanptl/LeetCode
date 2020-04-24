def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key = lambda x: x[0])
        cs = intervals[0][0]
        ce = intervals[0][1]
        
        for i in range(1,len(intervals)):
            if intervals[i][0] >= cs and intervals[i][1] <= ce:
                count += 1
            elif intervals[i][0] <= ce:
                cs = min(cs, intervals[i][0])
                ce = max(ce, intervals[i][1])
        
        return len(intervals) - count