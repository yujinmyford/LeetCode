# DFS
# Runtime: O(m*n), where m and n are the number of rows and columns
# Space: O(m*n), for pacific and atlantic

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        pacific = set()
        atlantic = set()
   
        for i in range(row):
            self.dfs(pacific, i, 0, row, col, matrix)
        for i in range(row):
            self.dfs(atlantic, i, col - 1, row, col, matrix)
        for j in range(col):
            self.dfs(pacific, 0, j, row, col, matrix)
        for j in range(col):
            self.dfs(atlantic, row - 1, j, row, col, matrix)

        visited_both = pacific.intersection(atlantic)
        return list(visited_both)

    def dfs(self, visited, x, y, row, col, matrix):
        visited.add(x, y)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for add_x, add_y in directions:
            new_x = x + add_x
            new_y = y + add_y
            if 0 <= new_x <= row and 0 <= new_y <= col and (new_x, new_y) not in visited and matrix[new_x][new_y] >= matrix[x][y]:
                self.dfs(visited, new_x, new_y, row, col, matrix)

