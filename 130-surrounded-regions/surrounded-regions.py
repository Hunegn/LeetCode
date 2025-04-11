class Solution:
    def solve(self, board: List[List[str]]) -> None:

        """
        Do not return anything, modify board in-place instead.
        """
        dirc = [(-1,0),(0,-1),(0,1),(1,0)]
        def inbound(r,c):
            m = len(board)
            n = len(board[0])
            if 0<=r<m and 0<= c <n:
                return True
            return False
        surrounded = True
        visited = set()
        def dfs(visited, row, col):
            nonlocal surrounded
            visited.add((row,col))
            for row_change, col_change in dirc:
                new_row = row+row_change
                new_col = col+col_change
                if (new_row,new_col) not in visited:
                    if not inbound(new_row,new_col):
                        surrounded = False
                        return 
                    elif board[new_row][new_col] == 'O':
                        dfs(visited,new_row,new_col)
        def replace(visited, row, col):
            board[row][col] = 'X'
            visited.add((row,col))
            for row_change, col_change in dirc:
                new_row = row+row_change
                new_col = col+col_change
                if (new_row,new_col) not in visited:
                    if board[new_row][new_col] == 'O' and inbound(new_row,new_col):
                        replace(visited,new_row,new_col)
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    surrounded = True
                    dfs(set(),i,j)
                    print(i,j)
                    print(surrounded)
                    if surrounded:
                        replace(set(),i,j)
                
                
        