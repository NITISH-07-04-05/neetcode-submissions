from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return 

        rows = len(grid)
        columns = len(grid[0])

        queue = deque()

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 0 :
                    queue.append((r,c))

        directions = [(1,0),(-1,0),(0,1),(0,-1)]


        while queue:
            r,c = queue.popleft()

            for rc,cr in directions:
                nr = r + rc
                nc = c + cr

                if nr < 0 or nc < 0 or nr >= rows or nc >= columns:
                    continue
                
                
                if grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1

                    queue.append((nr,nc))


