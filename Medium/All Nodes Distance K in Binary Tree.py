def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
    from collections import deque
    def dfs(node, par = None):
        if node:
            node.par = par
            dfs(node.left, node)
            dfs(node.right, node)
    dfs(root)
    
    queue = deque([(target,0)])
    seen = {target}
    while queue:
        if queue[0][1] == K:
            return [n.val for n,d in queue]
        node,d = queue.popleft()
        for adj in (node.left, node.right, node.par):
            if adj and adj not in seen:
                seen.add(adj)
                queue.append((adj,d+1))
        
    return []