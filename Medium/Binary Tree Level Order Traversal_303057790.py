# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        a=collections.defaultdict(list)
        def tr(node, depth):
            if node:
                a[depth].append(node.val)
                if node.left:
                    tr(node.left, depth+1)
                if node.right:
                    tr(node.right, depth+1)
        tr(root,0)
        return a.values()
