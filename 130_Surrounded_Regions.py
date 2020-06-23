class Solution:
    def solve(self, board: List[List[str]]) -> None:
        from collections import deque
        """
        Do not return anything, modify board in-place instead.
        """
        # finding by circle (from outside to inside)
        if not board or not board[0]:
            return 
        
        # find all O on the edges first
        queue = deque([])
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and board[i][j] == 'O':
                    queue.append((i, j))
        
        # walk through queue
        # mark all O on the path as + which cannot change to X at the final round
        while queue:
            i, j = queue.popleft()
            if i >= 0 and i <= m-1 and j >= 0 and j <= n-1 and board[i][j] == 'O':
                board[i][j] = '+'
                queue.append((i - 1, j))
                queue.append((i + 1, j))
                queue.append((i, j - 1))
                queue.append((i, j + 1))
        # final check, O --> X, + --> O
        for i in range(m): 
            for j in range(n):
                if board[i][j] == '+':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        
                    
                    
                    
                    
                    
                
        
        