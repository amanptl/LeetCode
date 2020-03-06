class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        r = dict(Counter(ransomNote))
        m = dict(Counter(magazine))
        if(all(m.get(key,0)>=val for key,val in r.items())):
            return True
        return False
