import heapq
 
class Solution:
    def spanningTree(self, V, edges):
        adj = [[] for _ in range(V)]
        
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        
        visited = [False]*V
        mst_weight = 0
        min_heap = [(0,0)]
        
        while min_heap:
            weight, node = heapq.heappop(min_heap)
            
            if visited[node]:
                continue  
            
            visited[node] = True
            mst_weight += weight
            
            for nei,w in adj[node]:
                if not visited[nei]:
                    heapq.heappush(min_heap,(w,nei))
        
        return mst_weight