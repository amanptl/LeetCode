def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        visited = [False] * (N+1)
        path = {}
        # Create graph
        for node1, node2 in dislikes:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        # Detect cycle, if no cycle return True else False
        def isCycleUtil(node, visited, parent, path, path_len):
            visited[node] = True
            path[node] = path_len
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    if isCycleUtil(neighbor, visited, node, path, path_len + 1):
                        return True
                elif parent != neighbor:
                    if neighbor in path and (path_len - path[neighbor]) % 2 == 0:
                        return True
            path.pop(node)
            return False
                
        
        def isCyclic():
            for node in graph:
                if not visited[node]:
                    if isCycleUtil(node, visited, -1, path, 0):
                        return False
            return True
        
        return isCyclic()