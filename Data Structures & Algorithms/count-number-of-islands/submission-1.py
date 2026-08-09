class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 

        rows = len(grid)
        columns = len(grid[0])

        visited = set()

        def dfs(r,c):

            if r<0 or c < 0 or r >= rows or c >= columns:
                return 

            elif grid[r][c] == "0":
                return 

            elif (r,c) in visited:
                return 

            visited.add((r,c))

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        island = 0

        for r in range(rows):
            for c in range(columns):

                if grid[r][c] is "1" and (r,c) not in visited:
                    dfs(r,c)

                    island +=1

        return island
