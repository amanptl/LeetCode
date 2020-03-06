class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        currList = []
        top = []
        bottom = []
        total = 0
        
        for i in range(len(grid)):
            currList = []
            for j in range(len(grid[i])):
                currList.append(grid[i][j])
            top.append(max(currList))
        
        for i in range(len(grid)):
            currList = []
            for j in range(len(grid[i])):
                currList.append(grid[j][i])
            bottom.append(max(currList))
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                temp = min(top[i], bottom[j])
                total += temp - grid[i][j]
                grid[i][j] = temp
        print(grid)
        
        return total
