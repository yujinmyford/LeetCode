class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(row, col, i, cycle):
            if i  == len(word):
                return True
                
            if(
                row not in range(len(board))
                or col not in range(len(board[0]))
                or i not in range(len(word))
                or board[row][col] != word[i]
                or (row, col) in cycle
            ):
                return False
            
            
            
            cycle.add((row, col))
            res = dfs(row + 1, col, i + 1, cycle) or dfs(row - 1, col, i + 1, cycle) or dfs(row, col + 1, i + 1, cycle) or dfs(row, col - 1, i + 1, cycle)
            cycle.remove((row, col))
            return res

        cycle = set()        

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0, cycle):
                    return True
        
        return False



# Backtracking, DFS
# Runtime: O(n * m)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= row or c >= col or word[i] != board[r][c] or (r, c) in path):
                return False
            
            path.add((r,c))

            res = (dfs(r + 1, c, i + 1) or 
                    dfs(r - 1, c, i + 1) or 
                    dfs(r, c + 1, i + 1) or 
                    dfs(r, c - 1, i + 1))
            
            path.remove((r, c))
            return res
        
        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        
        return False
