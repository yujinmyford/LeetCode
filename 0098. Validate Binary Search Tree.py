# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Binary Search Tree
# Runtime: O(n)
# Space: O(1)
class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._isValidBST(root, float(-inf), float(inf))

    def _isValidBST(self, cur_node, lower_bound, upper_bound):
        # check if empty, then return True if it is
        if not cur_node:
            return True
        # make sure we meed bounds for BST
        if not (lower_bound < cur_node.val and cur_node.val < upper_bound):
            return False
        # recursive, send to left and right
        return self._isValidBST(cur_node.left, lower_bound, cur_node.val) and self._isValidBST(cur_node.right, cur_node.val, upper_bound)
