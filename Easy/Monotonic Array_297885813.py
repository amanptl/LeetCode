class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if all(A[i]<=A[i+1] for i in range(len(A)-1) ):
            return True
        elif all(A[i]>=A[i+1] for i in range(len(A)-1)):
            return True
        return False
