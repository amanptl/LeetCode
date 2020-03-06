class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        if(all(dict(Counter(magazine)).get(key,0)>=val for key,val in dict(Counter(ransomNote)).items())):
            return True
        return False
