class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:

        queue = deque()
        length = 0
        queue.append((0,0))
        visit = set()
        visit.add((0,0))

        ROWS = len(grid)
        COLS = len(grid[0])

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length

                neighbours = [[0 , 1], [0, -1], [1, 0], [-1, 0]]

                for (i,j) in neighbours:
                    if min(r + i, c + j) < 0 or r + i >= ROWS or c + j >= COLS or (r + i, c + j) in visit or grid[r+i][c+j] == 1:
                        continue
                    
                    queue.append((r+i, c+j))
                    visit.add((r + i, c + j))
                
            length = length + 1
        
        return -1


                
                




