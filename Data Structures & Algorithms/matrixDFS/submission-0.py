class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])

        def dfs(grid: List[List[int]], r: int, c: int, visit: set) -> int:
            if min(r,c) < 0 or r >= N or c >= M or grid[r][c] == 1 or (r,c) in visit:
                return 0
            if r == N - 1 and c == M - 1:
                return 1
            visit.add((r,c))
            count = 0
            count += dfs(grid, r, c + 1, visit)
            count += dfs(grid, r - 1, c, visit)
            count += dfs(grid, r + 1, c, visit)
            count += dfs(grid, r, c - 1, visit)
            visit.remove((r,c))
            return count

        ans = dfs(grid, 0, 0, set())
        return ans
    

    
    

