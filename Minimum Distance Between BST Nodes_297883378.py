# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        nodes = []
        def dfs(node):
            if node:
                nodes.append(node.val)
                if node.left:
                    dfs(node.left)
                if node.right:
                    dfs(node.right)
        
        dfs(root)
        return (min(abs(a-b) for a in nodes for b in nodes if a!=b))
