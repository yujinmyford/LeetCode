# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BST, DFS
# Runtime: O(n)
# Space: O(1)

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        diff = abs(left - right)
        if diff > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    
    def dfs(self, root) -> int:
        if not root:
            return 0
        
        return 1 + max(self.dfs(root.left), self.dfs(root.right))
