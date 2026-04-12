class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [0] * n
        count = n
        for u, v in edges:
            p1 = parent[u]
            p2 = parent[v]

            if p1 != p2:
                if rank[p2] > rank[p1]:
                    parent[p1] = p2
                    rank[p2] += 1
                else:
                    parent[p2] = p1
                    rank[p1] += 1
                count -= 1
        
        return 1 if count == 0 else count

        