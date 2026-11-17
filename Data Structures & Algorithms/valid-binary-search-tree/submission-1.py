# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # bfs
        # all left vals < node 
        # all right vals > node
        if not root:
            return True
        def dfs(root, minVal, maxVal):
            if not root:
                return True
            if minVal >= root.val or root.val >= maxVal:
                return False
            left = dfs(root.left, minVal, root.val)
            right = dfs(root.right, root.val, maxVal)
            return left and right
        return dfs(root, float('-inf'), float('inf'))
