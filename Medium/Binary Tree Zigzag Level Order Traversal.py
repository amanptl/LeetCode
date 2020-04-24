def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import defaultdict
        res = defaultdict(list)
        def travel(node,level):
            if node:
                res[level].append(node.val)
                if node.left:
                    travel(node.left,level+1)
                if node.right:
                    travel(node.right,level+1)
        
        travel(root,0)
        d = []
        for i in range(len(res)):
            if i % 2:
                d.append(res[i][::-1])
            else:
                d.append(res[i])
        return d