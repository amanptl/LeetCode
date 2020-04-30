def maxPathSum(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0
            
            left = max(0,dfs(node.left))
            right = max(0,dfs(node.right))
            
            self.m = max(self.m, left + right + node.val)
            
            return max(left, right) + node.val
        
        self.m = float('-inf')
        
        dfs(root)
        
        return self.m