def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        def deserialize(preorder,limit):
            if preorder and preorder[0] < limit:
                val = preorder.pop(0)
                node = TreeNode(val)
                node.left = deserialize(preorder,val)
                node.right = deserialize(preorder,limit)
                return node
            return None
            
            
        return deserialize(preorder,float('inf'))