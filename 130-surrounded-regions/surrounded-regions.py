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
                
                if not inbound(new_row,new_col):
                        surrounded = False
                        
                elif (new_row,new_col) not in visited:
                    
                    if board[new_row][new_col] == 'O':
                        dfs(visited,new_row,new_col)
        def replace(visiteds, row, col):
            board[row][col] = 'X'
            visiteds.add((row,col))
            for row_change, col_change in dirc:
                new_row = row+row_change
                new_col = col+col_change
                if (new_row,new_col) not in visiteds:
                    if board[new_row][new_col] == 'O' and inbound(new_row,new_col):
                        replace(visiteds,new_row,new_col)
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i,j) not in visited:
                    surrounded = True
                    dfs(visited,i,j)
                    if surrounded:
                        replace(set(),i,j)
                
                
        