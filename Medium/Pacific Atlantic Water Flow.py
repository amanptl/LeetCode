def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        self.directions = ((0,-1), (0,1), (1,0), (-1,0))
        rows = len(matrix)
        cols = len(matrix[0])
        pacific = set()
        atlantic = set()
        res = []
        for i in range(rows):
            self.dfs(matrix,pacific,i,0,rows,cols)
            self.dfs(matrix,atlantic,i,cols-1,rows,cols)
        for j in range(cols):
            self.dfs(matrix,pacific,0,j,rows,cols)
            self.dfs(matrix,atlantic,rows-1,j,rows,cols)
        for i in range(rows):
            for j in range(cols):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append([i,j])
        return res
        
        
    def dfs(self,matrix,visited,i,j,rows,cols):
        visited.add((i,j))
        for direction in self.directions:
            n_i, n_j = i + direction[0], j + direction[1]
            if n_i < 0 or n_i >= rows or n_j < 0 or n_j >= cols or (n_i,n_j) in visited or matrix[n_i][n_j] < matrix[i][j]:
                continue
            self.dfs(matrix,visited,n_i,n_j,rows,cols)