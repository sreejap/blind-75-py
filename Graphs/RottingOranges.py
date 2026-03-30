from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # use bfs , this is multi source bfs
        if not grid:
            return -1

        rows = len (grid)
        cols = len (grid[0])

        minutes = 0
        queue = deque () # initilaizing empty queue
        fresh = 0
        for i in range (rows):
            for j in range (cols):
                if grid [i][j] == 2:
                    queue.append((i,j))

                elif grid [i][j] == 1:
                    fresh += 1


        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        while queue and fresh > 0:     # add a conditon that fresh should be > 0    
            curr_queue = len (queue)
            for i in range (curr_queue):
                x,y = queue.popleft()   
                for d in dirs:
                    nx1 = x + d[0] # use nx, ny instead
                    ny1 = y + d[1]
                    if 0 <= nx1 < rows and 0 <= ny1 < cols and grid [nx1][ny1] == 1:
                        grid [nx1][ny1] = 2
                        fresh -= 1
                        queue.append ((nx1,ny1))
            minutes += 1 # we covered all neighbors in this level                       

        return minutes if fresh == 0 else -1
