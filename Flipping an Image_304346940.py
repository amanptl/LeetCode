class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for r in range(len(A)):
            A[r] = A[r][::-1]
        for r in range(len(A)):
            for c in range(len(A[r])):
                if A[r][c] == 0:
                    A[r][c] = 1
                else:
                    A[r][c] = 0
        return A
