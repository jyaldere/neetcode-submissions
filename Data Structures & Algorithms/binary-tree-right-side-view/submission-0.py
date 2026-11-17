# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 'visible from right' is a right node OR if no right node, then the next one BFS
        if not root:
            return []
        levels = []
        queue = deque([root])
        while len(queue) > 0:
            level = []

            for i in range(len(queue)):
                    node = queue.popleft()
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            levels.append(level)
        result = []
        for level in levels:
            result.append(level[-1])
        return result

                

        