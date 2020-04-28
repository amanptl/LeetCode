def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        
        root.right = left
        root.left = right
        
        return root