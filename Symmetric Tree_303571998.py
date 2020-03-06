# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        a=collections.defaultdict(list)
        def t(node,depth):
            if node:
                a[depth].append(node.val)
                t(node.left,depth+1)
                t(node.right,depth+1)
            else:
                a[depth].append(-1)
        t(root,0)
        print(a)
        for i in a.keys():
            if a[i] != a[i][::-1]:
                return False
        return True
