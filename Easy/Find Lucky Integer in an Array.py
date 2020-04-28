def findLucky(self, arr: List[int]) -> int:
        d = {}
        for num in arr:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        res = float('-inf')
        for entry in d:
            if entry == d[entry]:
                res = max(res,entry)
        if res == float('-inf'):
            return -1
        return res