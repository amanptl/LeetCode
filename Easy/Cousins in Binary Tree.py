from collections import deque
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root or root.val == x or root.val == y:
            return False
        q = deque([root])
        
        while q:
            size = len(q)
            is_x = False
            is_y = False
            for _ in range(size):
                node = q.popleft()
                if node.val == x:
                    is_x = True
                elif node.val == y:
                    is_y = True
                if node.left and node.right:
                    if set([node.left.val, node.right.val]) == set([x,y]):
                        return False
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)   
            if is_x and is_y:
                    return True
        return False