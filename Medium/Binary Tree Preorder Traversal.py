def preorderTraversal(self, root: TreeNode) -> List[int]:
        a = []
        def pre(node):
            if node:
                a.append(node.val)
                if node.left:
                    pre(node.left)
                if node.right:
                    pre(node.right)
        pre(root)
        return a