def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1
        trusted = [0]*(N+1)
        
        for a,b in trust:
            trusted[a] -= 1
            trusted[b] += 1
        
        for i in range(N+1):
            if trusted[i] == N-1:
                return i
        return -1