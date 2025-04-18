class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == newColor:
            return image

        def dfs(r, c):
            if (0 <= r < len(image)) and (0 <= c < len(image[0])) and image[r][c] == original_color:
                image[r][c] = newColor
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)

        dfs(sr, sc)
        return image
