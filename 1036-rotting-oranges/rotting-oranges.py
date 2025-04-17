class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirc = ((-1,0),(0,-1),(0,1),(1,0))
        time = 0
        m = len(grid)
        n = len(grid[0])
        def inbound(row,col):
            nonlocal m
            nonlocal n
            if 0<=row<m and 0<=col< n: return True
            return False
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append(((i,j),0))
        time = 0
        while queue:
            node,level = queue.popleft()
            
            row,col = node
            for row_change, col_change in dirc:
                new_row, new_col = row+row_change, col+col_change
                
                if inbound(new_row,new_col) and grid[new_row][new_col] == 1:
                    time = max(time,level+1)
                    
                    grid[new_row][new_col] = 2
                    queue.append(((new_row,new_col),level+1))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return time
                



