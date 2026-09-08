class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        colms = len(grid[0])
        islands = 0
        visited = set()

        def dfs(grid, i, j):
            if i < 0 or i > rows-1 or j < 0 or j > colms-1 or (grid[i][j] == "0") or (i,j) in visited:
                return
            elif grid[i][j] == "1":
                visited.add((i,j))

            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)
  
        for i in range(rows):
            for j in range(colms):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(grid, i, j)
                    islands += 1

        return islands

        