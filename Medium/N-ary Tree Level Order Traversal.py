def levelOrder(self, root: 'Node') -> List[List[int]]:
        from collections import defaultdict
        d = defaultdict(list)
        def dfs(node,level):
            if node:
                d[level].append(node.val)
                for child in node.children:
                    if child:
                        dfs(child,level+1)
        dfs(root,0)
        res = []
        for l in d:
            res.append(d[l])
        return res