# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        self.res = None

        def dfs(one, two):
            if not one or not two:
                return
            if one is target:
                self.res = two
            dfs(one.left, two.left)
            dfs(one.right, two.right)
        
        dfs(original, cloned)
        return self.res
