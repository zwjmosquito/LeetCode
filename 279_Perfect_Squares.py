class Solution:
    def numSquares(self, n: int) -> int:
        ##### Method 1: DP ## 5280ms
        # dp[i] --- least number of perfect square numbers sum to i
        # dp[i+1] = dp[i] + 1 or dp[i-4] + 1 or dp[i-9] + 1
        
        dp = [i for i in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, i):
                if j*j > i:
                    break
                dp[i] = min(dp[i], dp[i - j*j] + 1)
        
        return dp[-1]
    
        #### Method 2: BFS ## 196ms
        # each layer stores numbers that current investigate
        
        nodes = set([n])
        # create a dictionary of all squares
        squares = [i**2 for i in range(int(n**0.5) + 1)]
        d = 1
        
        while nodes:
            cur = set() # use set other than list makes it faster (avoid duplicates)
            for node in nodes:
                for square in squares:
                    if node == square: return d
                    if node < square: break
                    
                    cur.add(node - square)
            
            nodes, d = cur, d + 1
        
        return d
            
        
        
                
            
        