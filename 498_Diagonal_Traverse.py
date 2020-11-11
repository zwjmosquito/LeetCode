class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        # brute force
        if not matrix or not matrix[0]:
            return matrix
        
        x, y, dr = 0, 0, "r"
        M, N = len(matrix), len(matrix[0])
        
        res = []
        while x < M and y < N:
            res.append(matrix[x][y])
            
            if dr == "r":
                dx, dy = -1, 1
                x, y = x + dx, y + dy                
                if y >= N:
                    y = N - 1
                    x = x + 2
                    dr = "l"
                elif x < 0:
                    x = 0
                    dr = "l"
                
            else:
                dx, dy = 1, -1
                x, y = x + dx, y + dy
                if x >= M:
                    x = M - 1
                    y = y + 2
                    dr = "r"
                    
                elif y < 0:
                    y = 0
                    dr = "r"
        
        return res



        ### Method 2 ###
        # same diagonal share the same index sum
        from collections import defaultdict
        store = defaultdict(list)
        
        if not matrix or not matrix[0]:
            return matrix
        M, N = len(matrix), len(matrix[0])
        
        for i in range(M):
            for j in range(N):
                store[i+j].append(matrix[i][j])
        
        res = []
        for i in range(len(store.keys())):
            if i%2 == 0:
                res += store[i][::-1]
            else:
                res += store[i]
        
        return res