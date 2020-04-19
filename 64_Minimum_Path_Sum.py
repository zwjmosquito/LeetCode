class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        # dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        # instead of use if-else conditions in the for loop, 
        # seperate the initilization makes the code faster and easy to read
        for i in range(1, m):
            grid[i][0] = grid[i-1][0] + grid[i][0] 
        for j in range(1, n):
            grid[0][j] = grid[0][j-1] + grid[0][j] 
         
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
                    
        return grid[m-1][n-1]
                
              
        
        