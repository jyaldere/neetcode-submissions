# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:        

        def dfs(root):
            if root is None:
                return 0

            left_tree = dfs(root.left)
            right_tree = dfs(root.right)
            if left_tree == -1 or right_tree == -1:
                return -1
            if abs(left_tree - right_tree) > 1:
                return -1
            return 1 + max(left_tree, right_tree)
        
        height = dfs(root)
        if height == -1:
            return False
        return True