class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = {}
        
        for c in magazine:
            if c not in m:
                m[c] = 1
            else:
                m[c] += 1
        
        for c in ransomNote:
            if c not in m or m[c] < 1:
                return False
            else:
                m[c] -= 1
        
        return True
