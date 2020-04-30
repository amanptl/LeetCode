def minWindow(self, s: str, t: str) -> str:
        m = {}
        for c in t:
            if c in m:
                m[c] += 1
            else:
                m[c] = 1
        
        start, end = 0, 0
        counter = len(t)
        minStart = 0
        minLen = float('inf')
        size = len(s)
        
        while end < size:
            if s[end] in m:
                if m[s[end]] > 0:
                    counter -= 1
                m[s[end]] -= 1
            
            while counter == 0:
                if end - start + 1 < minLen:
                    minStart = start
                    minLen = end - start + 1
                if s[start] in m:
                    m[s[start]] += 1
                    if m[s[start]] > 0:
                        counter += 1
                start += 1
                
            end += 1
        if minLen != float('inf'):
            return s[minStart:minStart+minLen]
        return ''