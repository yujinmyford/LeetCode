# Runtime: O(n^2)
# Space: O(N)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                cur = board[r][c]
            
                # If cur is empty, or ".", just continue
                if cur == ".":
                    continue
            
                # If cur already exists in rows, cols, or squares, return False
                if (cur in rows[r]) or (cur in cols[c]) or (cur in squares[(r // 3, c // 3)]):
                    return False
            
                # Add cur to cols, rows, squares
                cols[c].add(cur)
                rows[r].add(cur)
                squares[(r // 3, c // 3)].add(cur)
        
        # If went through whole board without seeing duplicates, return True
        return True
