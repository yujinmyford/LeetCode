# Graph, DFS

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        maxArea = 0

        def dfs(grid, row, col):
            if (
                row not in range(rows)
                or col not in range(cols)
                or grid[row][col] == 0
                or (row, col) in visited               
            ):
                return 0
            
            visited.add((row, col))
            return 1 + dfs(grid, row + 1, col) + dfs(grid, row - 1, col) + dfs(grid, row, col + 1) + dfs(grid, row, col - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and grid[r][c] not in visited:
                    maxArea = max(maxArea, dfs(grid, r, c))
        
        return maxArea
