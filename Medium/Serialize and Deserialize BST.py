def serialize(self, root):
        if not root:
            return "X,"
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return str(root.val)+","+str(left)+str(right)
        

def deserialize(self, data):
    nodes = data.split(',')
    return self.helper(nodes)

def helper(self, nodes):
    val = nodes.pop(0)
    if val == 'X':
        return None
    new_node = TreeNode(int(val))
    new_node.left = self.helper(nodes)
    new_node.right = self.helper(nodes)
    return new_node