# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # basically the current node is >= all previous nodes in the tree
        # keep track of max ? 
        #dfs 
        # need counter
        count = 0
        maxVal = root.val
        def dfs(root, maxVal):
            nonlocal count
            if root is None:
                return 0 
            if root.val >= maxVal:
                maxVal = root.val
                count += 1
            left = dfs(root.left, maxVal)
            right = dfs(root.right, maxVal)
        dfs(root, maxVal)
        return count