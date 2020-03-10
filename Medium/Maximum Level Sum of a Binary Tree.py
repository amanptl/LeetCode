def maxLevelSum(self, root: TreeNode) -> int:
        a = {}
        def level(node,depth):
            if node:
                if depth in a:
                    a[depth]+=node.val
                else:
                    a[depth] = node.val
                if node.left:
                    level(node.left, depth+1)
                if node.right:
                    level(node.right, depth+1)
                
        level(root,1)
        m = 0
        index = 0
        for i in a:
            if a[i] > m:
                m = a[i]
                index = i
        return index