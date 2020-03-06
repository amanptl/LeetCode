class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        n = len(A)
        if n == len(B):
            b = A+A
            return B in b
        return False
