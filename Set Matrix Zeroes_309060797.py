class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        rowZ = False
        colZ = False
        
        def nullRow(i):
            for j in range(n):
                matrix[i][j]=0
        def nullCol(j):
            for i in range(m):
                matrix[i][j]=0

        for j in range(n):
            if matrix[0][j] == 0:
                rowZ = True
                break 
        for i in range(m):
            if matrix[i][0] == 0:
                colZ = True
                break
        #print(rowZ,colZ)
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        #print(matrix)
        for j in range(1,n):
            if matrix[0][j]==0:
                nullCol(j)
        #print(matrix)
        for i in range(1,m):
            if matrix[i][0]==0:
                nullRow(i)
        print(matrix)
        if rowZ==True:
            nullRow(0)
        if colZ==True:
            nullCol(0)



        
