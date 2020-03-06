# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        self.d = 0
        def dfs(node, depth):
            if node:
                if self.d < depth:
                    self.d = depth
                if node.left:
                    dfs(node.left, depth+1)
                if node.right:
                    dfs(node.right, depth+1)
        dfs(root,1)
        return self.d
