class Solution:

    # DFS with Cache
    def cherryPickup(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])

        cache = {}
        
        def dfs(r, c1, c2):

            if (r, c1, c2) in cache:
                return cache[(r, c1, c2)]

            if c1 == c2 or min(c1, c2) < 0 or max(c1, c2) == COLS:
                return 0
            
            if r == ROWS - 1:
                return grid[r][c1] + grid[r][c2]
            
            res = 0

            for c1_d in [-1, 0, 1]:
                for c2_d in [-1, 0, 1]:
                    res = max(
                        res,
                        dfs(r + 1, c1 + c1_d, c2 + c2_d)
                    )
                    
            cache[(r, c1, c2)] = res + grid[r][c1] + grid[r][c2]
            return cache[(r, c1, c2)]
        
        return dfs(0, 0, COLS - 1)



    # DP, bottom-up
    def cherryPickup(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])

        dp = [[0] * COLS for i in range(COLS)]

        for r in reversed(range(ROWS)):
            curDP = [[0] * COLS for i in range(COLS)]

            for c1 in range(COLS - 1):
                for c2 in range(c1 + 1, COLS):
                    maxCherries = 0
                    cherries = grid[r][c1] + grid[r][c2]
                    for c1d in [-1, 0, 1]:
                        for c2d in [-1, 0, 1]:
                            nc1, nc2 = c1 + c1d, c2 + c2d
                            if nc1 < 0 or nc2 == COLS:
                                continue
                            maxCherries = max(
                                maxCherries,
                                cherries + dp[nc1][nc2]
                            )


                    curDP[c1][c2] = maxCherries
            dp = curDP
        
        return dp[0][COLS - 1]
