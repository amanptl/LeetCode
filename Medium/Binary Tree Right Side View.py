def rightSideView(self, root: TreeNode) -> List[int]:
        from collections import defaultdict
        res = defaultdict(list)
        def dfs(node,level):
            if node:
                res[level].append(node.val)
                dfs(node.left,level+1)
                dfs(node.right,level+1)
        dfs(root,0)
        ans = []
        for i in res:
            ans.append(res[i][-1])
        return ans