class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # dp[i][v] -- longest length end with i, with interval v
        dp = {} # a dictionary of dictionary, outer key, i, inner key v
        res = 1
        for i in range(len(A)):
            dp[i] = {}
            for j in range(i):
                v = A[i] - A[j]
                if v in dp[j]: 
                    dp[i][v] = dp[j][v] + 1
                else:
                    dp[i][v] = 2
                res = max(res, dp[i][v])
        return res
                    
        
        