# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        a=[]
        #l R r
        def inorder(node):
            if node:
                if node.left:
                    inorder(node.left)
                a.append(node.val)
                if node.right:
                    inorder(node.right)
        inorder(root)
        return a
