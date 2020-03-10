def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        a = []
        while stack:
            node = stack.pop()
            if node:
                a.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return a[::-1]