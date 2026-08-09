class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = []
        atlantic = []
        pacific_vis = set()
        atlantic_vis = set()

        rows = len(heights)
        columns = len(heights[0])

        for c in range(columns):
            pacific.append((0,c))

        for r in range(rows):
            pacific.append((r,0))

        for c in range(columns):
            atlantic.append((rows-1,c))

        for r in range(rows):
            atlantic.append((r,columns-1))

        def bfs(starts,ocean):

            queue = deque(starts)

            for temp in starts:
                ocean.add(temp)

            while queue:

                r,c = queue.popleft()

                for dr , dc in [(1,0),(-1,0),(0,1),(0,-1)]:

                    nr,nc = r + dr , c + dc

                    if nr < 0 or nr >= rows or nc < 0 or nc >= columns:
                        continue

                    if heights[nr][nc] < heights[r][c]:
                        continue
                    if (nr,nc) in ocean:
                        continue
                    queue.append((nr,nc))
                    ocean.add((nr,nc))

        bfs(pacific,pacific_vis)
        bfs(atlantic,atlantic_vis)

        result = []

        for r in range(rows):
            for c in range(columns):
                if (r,c) in pacific_vis and (r,c) in atlantic_vis:
                    result.append([r,c])
        
        return result
            



        