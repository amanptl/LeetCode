def isBalanced(self, root: TreeNode) -> bool:
        return self.check(root)[0]
    
    def check(self, node):
        if not node:
            return [True, -1]
        
        left = self.check(node.left)
        if not left[0]:
            return left
        
        right = self.check(node.right)
        if not right[0]:
            return right
        
        h = max(left[1],right[1]) + 1
        return [abs(left[1] - right[1]) <= 1, h]