# Array
# Runtime: O(m*n), for the rows and columns
# Space: O(n)

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col =  len(grid[0])
        perimeter = 0
        
        # Traverse through grid
        for i in range(row):
            for j in range(col):
                # If the cell we are on is land, increment by 4
                if grid[i][j] == 1: 
                    perimeter += 4
                # Check top cell, if it is land decrement by 2
                    if i >= 1 and grid[i-1][j] == 1:
                        perimeter -= 2
                # Check left cell, if it is land decrement by 2
                    if j >= 1 and grid[i][j-1] == 1:
                        perimeter -= 2
        return perimeter
