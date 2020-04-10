def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            self.ans = max(self.ans, l+r+1)
            return max(l,r) + 1
        self.ans = 1
        dfs(root)
        return self.ans - 1