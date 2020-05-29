def frequencySort(self, s: str) -> str:
        ans = ''
        d = {}
        
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        
        for w in sorted(d, key=d.get, reverse=True):
            ans += w * d[w]
            
        return ans