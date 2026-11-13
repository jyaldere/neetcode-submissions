# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
         # for each node, we need to swap its children. but the children need to also move places with its parent. im not sure what conceptually would be best, DFS? until u reach a parent with only leaf children?
        node = root   
        if node == None:
            return
        temp_left = node.left
        node.left = node.right
        node.right = temp_left
        self.invertTree(node.left)
        self.invertTree(node.right)
        return node