class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        colms = len(grid[0])
        visited = set()
        max_area = 0
        curr_area = 0
        def dfs(grid, i , j):
            nonlocal curr_area
            if i < 0 or i > rows-1 or j<0 or j>colms-1 or grid[i][j] == 0 or (i,j) in visited:
                return
            elif grid[i][j] == 1:
                curr_area += 1
                visited.add((i,j))

            dfs(grid, i+1 , j)
            dfs(grid, i-1 , j)
            dfs(grid, i , j+1)
            dfs(grid, i , j-1)

        for i in range(rows):
            for j in range(colms):
                if grid[i][j] == 1 and (i,j) not in visited:
                    curr_area = 0
                    dfs(grid, i , j)
                    max_area = max(max_area, curr_area)

        return max_area

