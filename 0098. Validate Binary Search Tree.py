# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BST, recursion
# Runtime: O(n)
# Space: O(1)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float('-inf'), float('inf'))
        
    
    def validate(self, root: TreeNode, lower: int, upper: int):
        if not root:
            return True
        if not (lower < root.val < upper):
            return False
        return self.validate(root.left, lower, root.val) and self.validate(root.right, root.val, upper)
