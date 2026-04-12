class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj = {c : [] for c in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(v, prev):
            if v in visit:
                return False
            visit.add(v)
            for nei in adj[v]:
                if nei == prev:
                    continue
                if not dfs(nei, v):
                    return False
            return True
        
        
        return dfs(0, -1) and len(visit) == n
