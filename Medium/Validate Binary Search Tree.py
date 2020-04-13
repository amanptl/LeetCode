def isValidBST(self, root: TreeNode) -> bool:
        res = []
        def inorder(node):
            if node:
                if node.left:
                    inorder(node.left)
                res.append(node.val)
                if node.right:
                    inorder(node.right)
        inorder(root)
        print(res)
        for i in range(1,len(res)):
            if res[i] <= res[i-1]:
                return False
        return True