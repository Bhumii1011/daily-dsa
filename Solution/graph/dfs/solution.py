class Solution:
    def dfs(self, adj):
        v =len(adj)
        visited = [False]*v
        result = []
        
        def dfsUtil(node):
            visited[node] =True
            result.append(node)
            
            for nei in adj[node]:
                if not visited[nei]:
                    dfsUtil(nei)
            
        dfsUtil(0)
        return result