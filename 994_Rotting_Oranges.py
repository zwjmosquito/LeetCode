class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS
        
        # first find rotten positions
        rotten = []
        orange = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten += [(i, j)]
                elif grid[i][j] == 1:
                    orange += 1

        if not orange:
            return 0
        elif len(rotten) == 0 and orange:
            return -1
        
        
        current_grid = grid.copy()
        time = 0
        
        while rotten:
            tmp = []
            for i, j in rotten:
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    x, y = i + dx, j + dy
                    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or current_grid[x][y] == 2 or current_grid[x][y] == 0:
                        continue
                    tmp += [(x, y)]
                    current_grid[x][y] = 2
                    orange -= 1
            time += 1
            rotten = tmp
        
        if orange > 0: # still exists orange
            return -1
        return time - 1
                        
            
            
        
        