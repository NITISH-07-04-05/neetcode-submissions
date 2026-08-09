class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if grid is None:
            return 

        rows = len(grid)
        columns = len(grid[0])

        queue = deque()
        fresh = 0
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        minutes = 0

        while queue:

            is_rotten = False

            for _ in range(len(queue)):
                r,c = queue.popleft()
                
                for rr, cc in directions:

                    nr = r + rr
                    nc = c + cc

                    if nr < 0 or nr >= rows or nc < 0 or nc >= columns:
                        continue

                    if grid[nr][nc] != 1:
                        continue 

                    elif grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1

                        queue.append((nr,nc))
                        is_rotten = True

            if is_rotten == True:
                minutes += 1

        return minutes if minutes and fresh == 0 else -1

                


            
            