def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ''
        def foo(l):
            s = strs[0][0:l]
            for i in range(1, len(strs)):
                if not strs[i].startswith(s):
                    return False
            return True
        
        min_ = float('inf')
        for s in strs:
            min_ = min(min_, len(s))
        lo = 1
        hi = min_
        while lo <= hi:
            mid = (lo + hi) // 2
            if foo(mid):
                lo = mid + 1
            else:
                hi = mid - 1
        return strs[0][0:(lo+hi)//2]