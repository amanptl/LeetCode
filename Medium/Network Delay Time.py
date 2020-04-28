def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        from collections import defaultdict
        
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append([v,w])
        
        pq = [(0, K)]
        dist = {}
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist: continue
            dist[node] = d
            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d+d2, nei))

        return max(dist.values()) if len(dist) == N else -1