# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.total=0
        self.max_ = 0
        def dfs(node,depth):
            if node:
                if depth > self.max_:
                    self.max_ = depth
                    self.total = node.val
                elif depth == self.max_:
                    self.total += node.val
                if node.left:
                    dfs(node.left, depth+1)
                if node.right:
                    dfs(node.right, depth+1)             
        dfs(root, 1)
        return self.total
