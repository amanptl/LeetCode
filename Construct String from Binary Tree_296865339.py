# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        stack = []
        def fun(node):
            if node:
                stack.append(str(node.val))
                if node.left:
                    stack.append('(')
                    fun(node.left)
                    stack.append(')')
                if node.right:
                    if node.left == None:
                        stack.append('()')
                    stack.append('(')
                    fun(node.right)
                    stack.append(')')
        
        fun(t)
        return ''.join(stack)
