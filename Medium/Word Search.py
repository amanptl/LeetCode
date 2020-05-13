def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        
        def traverse(x,y,i):
            if i == len(word):
                return True
            if x > (len(board)-1) or x < 0 or y < 0 or y > (len(board[0])-1) or board[x][y] != word[i]:
                return False
            board[x][y] = '*'
            res = False
            for dx, dy in directions:
                res = res or traverse(x+dx, y+dy, i+1)
            board[x][y] = word[i]
            return res
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if traverse(i,j,0):
                    return True
        return False