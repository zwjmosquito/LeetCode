from typing import List

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        M, N = len(A), len(A[0])
        B = [[0 for _ in range(M)] for _ in range(N)]
        for i in range(M):
            for j in range(N):
                B[j][i] = A[i][j]
                
        return B