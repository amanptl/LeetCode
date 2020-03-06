class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a = []*numRows
        for i in range(numRows):
            t = [1]*(i+1)
            a.append(t)
            for j in range(1,i):
                t[j] = a[i-1][j-1]+a[i-1][j]
             
        return a
