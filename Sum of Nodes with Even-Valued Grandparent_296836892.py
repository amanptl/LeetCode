# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(N):
            if N and not N.val % 2:
                if N.left:
                    if N.left.left:  self.total += N.left.left.val
                    if N.left.right: self.total += N.left.right.val
                if N.right:
                    if N.right.left:  self.total += N.right.left.val
                    if N.right.right: self.total += N.right.right.val
            if N: dfs(N.left), dfs(N.right)
        self.total = 0
        dfs(root)
        return self.total       
            
                
                
