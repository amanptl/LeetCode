class Solution:
    def titleToNumber(self, s: str) -> int:
        t = 0
        for c in s:
            t = (t*26) + ord(c) - ord('A') + 1
        return t
