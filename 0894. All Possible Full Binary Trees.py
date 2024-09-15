# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

        # For cache
        dp = {}
        
        # Return list of full binary tress with n nodes
        def dfs(n):
            if n == 0:
                return []
            if n == 1:
                return [TreeNode()]
            
            if n in dp:
                return dp[n]
            
            res = []
            for left in range(n):
                right = n - 1 - left
                leftTrees, rightTrees = dfs(left), dfs(right)

                for t1 in leftTrees:
                    for t2 in rightTrees:
                        res.append(TreeNode(0, t1, t2))
            
            dp[n] = res
            return dp[n]
        
        return dfs(n)
