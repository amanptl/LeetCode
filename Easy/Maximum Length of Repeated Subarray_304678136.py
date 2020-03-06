class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        m = 0
        for i in range(len(A)-1,-1,-1):
            for j in range(len(B)-1,-1,-1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1]+1
                    if m < dp[i][j]:
                        m = dp[i][j]
        return m
