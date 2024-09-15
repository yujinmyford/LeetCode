# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        
        q = deque()
        q.append(root)
        maxLevel = 0
        maxSum = float('-inf')
        curLevel = 0
        
        while len(q) > 0:
            curLevel += 1
            curSum = 0
            
            for i in range(len(q)):
                curNode = q.popleft()
                if curNode:
                    curSum += curNode.val
                if curNode.left:
                    q.append(curNode.left)
                if curNode.right:
                    q.append(curNode.right)
            if curSum > maxSum:
                maxSum = curSum
                maxLevel = curLevel
        
        return maxLevel
