def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        nodeCopy = Node(node.val)
        d ={node:nodeCopy}
        queue = collections.deque([node])
        
        while queue:
            node = queue.popleft()
            for nei in node.neighbors:
                if nei not in d:
                    neiCopy = Node(nei.val)
                    d[nei] = neiCopy
                    d[node].neighbors.append(neiCopy)
                    queue.append(nei)
                else:
                    d[node].neighbors.append(d[nei])
        
        return nodeCopy