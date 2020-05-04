def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])
        curr_e = float('-inf')
        count = 0
        for s,e in intervals:
            if s < curr_e:
                count += 1
                curr_e = min(e, curr_e)
            else:
                curr_e = e
        return count