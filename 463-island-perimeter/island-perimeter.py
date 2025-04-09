class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dir = [(0,-1),(-1,0),(0,1),(1,0)]
        def inbound(row,col):
            return (0<=row<len(grid) and 0<=col<len(grid[0]))
        visited = [[False for col in row]  for row in grid]
        
        per = 0
        def dfs(visited,row,col):
            nonlocal per
            visited[row][col] = True
            for row_change, col_change in dir:
                new_row = row+row_change
                new_col = col+col_change
               
                if inbound(new_row,new_col) and grid[new_row][new_col]:
                    if not visited[new_row][new_col]:
                        dfs(visited,new_row,new_col)
                else:
                    per+=1
        for row in  range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    dfs(visited,row,col)
                    return per