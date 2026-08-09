class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if grid is None:
            return 

        rows = len(grid)
        columns = len(grid[0])

        visited = set()

        def dfs(r,c):

            if r < 0 or c < 0 or r >= rows or c >= columns:
                return 0

            if grid[r][c] == 0:
                return 0

            if (r,c) in visited:
                return 0

            visited.add((r,c))

            return 1+ dfs(r,c+1) +dfs(r,c-1) + dfs(r-1,c) + dfs(r+1,c)


        max_of_island = 0

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1 and (r,c) not in visited:
                    value = dfs(r,c)
                    max_of_island = max(value,max_of_island)

        return max_of_island