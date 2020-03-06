# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        a = []
        def inorder(node):
            if node:
                if node.left:
                    inorder(node.left)
                a.append(node.val)
                if node.right:
                    inorder(node.right)
        inorder(root)
        return a[k-1]
