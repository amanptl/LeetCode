class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = len(s1)
        seen = {''.join(sorted(s2[i:i+l])) for i in range(len(s2)-l+1)}
        s1 = ''.join(sorted(s1))
        if s1 in seen:
            return True
        return False
