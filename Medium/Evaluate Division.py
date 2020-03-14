import collections
def evalDiv(equations,values,queries):
    def dfs(graph,start,end,visited):
        print(start,end)
        if start == end and graph[start]:
                return 1.0
        visited.add(start)
        for adj,v in graph[start]:
            if adj in visited:
                continue
            temp = dfs(graph,adj,end,visited)
            if temp > 0:
                return v*temp
        return -1.0

    graph = collections.defaultdict(set)
    ans = []
    for item,v in zip(equations,values):
        x,y = item
        graph[x].add((y,v))
        graph[y].add((x,1/v))
    for start,end in queries:
        ans.append(dfs(graph,start,end,set()))
    return ans

print(evalDiv([["a","b"],["b","c"]],[2.0,3.0],[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))