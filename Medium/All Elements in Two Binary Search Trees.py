def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []
        def traverse(node):
            if node:
                if node.left:
                    traverse(node.left)
                res.append(node.val)
                if node.right:
                    traverse(node.right)
        
        traverse(root1)
        traverse(root2)
        
        return sorted(res)