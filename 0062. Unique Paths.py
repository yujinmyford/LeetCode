class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        visit = set()
        ROWS, COLS = m, n
        if (min(r, c) < 0 or
            r == ROWS or c == COLS or
            (r, c) in visit):
            return 0
        if r == ROWS - 1 and c == COLS - 1:
            return 1

        visit.add((r, c))

        count = 0
        count += self.uniquePaths(r + 1, c)
        count += self.uniquePaths(r - 1, c)
        count += self.uniquePaths(r, c + 1)
        count += self.uniquePaths(r, c - 1)

        visit.remove((r, c))
        return count



# DP, bottom up
# Runtime: O(m*n)
# Space: O(n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]
