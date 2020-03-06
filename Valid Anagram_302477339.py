class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        a = defaultdict(int)
        b = defaultdict(int)
        for i in s:
            a[i]+=1
        for i in t:
            b[i]+=1
        return a==b
        
