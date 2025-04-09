class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dir = [(0,-1),(-1,0),(0,1),(1,0)]
        def inbound(row,col):
            return (0<=row<len(grid) and 0<=col<len(grid[0]))
        visited = [[False for col in row]  for row in grid]
        
        area = 0
        new_area = 0
        def dfs(visited,row,col):
            nonlocal area
            nonlocal new_area
            visited[row][col] = True
            for row_change, col_change in dir:
                new_row = row+row_change
                new_col = col+col_change
               
                if inbound(new_row,new_col) and (grid[new_row][new_col]) and not visited[new_row][new_col]:
                    new_area +=1
                    dfs(visited,new_row,new_col)
            area = max(area,new_area)
        
        for row in  range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] and not visited[row][col]:
                    new_area  = 1
                    dfs(visited,row,col)          
        return area
        