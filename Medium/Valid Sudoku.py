def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        row_h = defaultdict(set)
        col_h = defaultdict(set)
        block_h = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row_h[i] or board[i][j] in col_h[j] or (i//3,j//3,board[i][j]) in block_h:
                        return False
                    row_h[i].add(board[i][j])
                    col_h[j].add(board[i][j])
                    block_h.add((i//3,j//3,board[i][j]))
        return True