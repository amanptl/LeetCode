class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:    
        def check(a,b):
            count = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    count += 1
            if count > 2:
                return False
            return True
        
        d = {}
        visited = []
        n = len(A)
        
        for i in range(n):
            d[i] = set()
            visited.append(False)
            for j in range(n):
                if i == j:
                    continue
                if check(A[i],A[j]):
                    d[i].add(j)
        
        groups = 0
        
        def dfs(v):
            visited[v] = True
            temp = [v]
            for i in d[v]:
                if visited[i] == False:
                    temp = dfs(i)
            return temp
        
        for v in range(n): 
            if visited[v] == False:
                if len(dfs(v)) > 0:
                    groups+=1
        
        return groups
        
            
         
##############################
class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:    
        import collections
        
        def check(x,y):
            count = 0
            for i in range(len(x)):
                if x[i] != y[i]:
                    count += 1
            if count > 2:
                return False
            return True
        
        def dfs(start):
            for i in range(len(A)):
                if A[i] in visited:
                    continue
                if check(start,A[i]):
                    visited.add(A[i])
                    dfs(A[i])
        
        graph = collections.defaultdict(set)
        visited = set()
        
        '''for x in A:
            for y in A:
                if x in graph[y]:
                    graph[x].add(y)
                elif check(x,y):
                    graph[x].add(y)
                else:
                    graph[x]
        
        groups = 0
        
        for vertex in graph:
            if vertex not in visited:
                dfs(vertex)
                groups+=1
        '''
        groups = 0
        for vertex in A:
            if(vertex in visited): 
                continue
            visited.add(vertex)
            dfs(vertex)
            groups += 1
        return groups
            
         
        
        