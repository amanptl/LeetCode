def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        dp = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        max_ = 0
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if matrix[i-1][j-1] == "0":
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
                max_ = max(dp[i][j],max_)
        print(dp)
        return max_**2 