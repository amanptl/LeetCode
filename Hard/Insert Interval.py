def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def merge():
            res = []
            curr_s = float('inf')
            curr_e = float('-inf')
            
            for s,e in intervals:
                if s <= curr_e:
                    curr_e = max(curr_e, e)
                    curr_s = min(curr_s, s)
                else:
                    res.append([curr_s, curr_e])
                    curr_s = s
                    curr_e = e

            res.append([curr_s, curr_e])
            return res[1:]
        intervals.append(newInterval)
        intervals.sort(key= lambda x:x[0])
        return merge()