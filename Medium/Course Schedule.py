def canFinish(numCourses, prerequisites):
    from collections import defaultdict
        
    if len(prerequisites)==0:
        return True
    
    graph = defaultdict(set)
    
    def cycleUtil(vertex,visited,stack):
        visited.add(vertex)
        stack.add(vertex)
        for adj in graph[vertex]:
            if adj not in visited:
                if cycleUtil(adj,visited,stack):
                    return True
            elif adj in stack:
                return True
        stack.remove(vertex)
        return False
                
        
    def cycle():
        visited = set()
        stack = set()
        for vertex in range(numCourses):
            if vertex not in visited:
                if cycleUtil(vertex,visited,stack):
                    return True
        return False
                
    
    for i in range(numCourses):
        graph[i]
        
    for course, req in prerequisites:
        graph[course].add(req)
    
    return not cycle()

print(canFinish(4,[[2,0],[1,0],[3,1],[3,2],[1,3]]))