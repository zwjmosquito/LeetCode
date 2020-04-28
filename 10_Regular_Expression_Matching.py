class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp
        # dp[i][j] - if s[:i] can be represented by p[:j]
        
        dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        # both s and p are ""
        dp[0][0] = True
        
        # initialize first row - s = "" and p has patten - `a*`
        for j in range(2, len(p)+1):
            # if p[j-1] == '*' and j-2 is True, then true
            dp[0][j] = dp[0][j-2] and p[j-1] == '*'
        
        # update dp
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                # if the current place equal or '.', then only depends on previous status
                if p[j-1] == s[i-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                # if current place is '*', then based on whther p[j-2] equal to s[i-1], there are different senarios
                elif p[j-1] == '*':
                    if p[j-2] != s[i-1] and p[j-2] != '.':
                        # if previous one is not match and not '.', then a* can only be interpret 0 time
                        dp[i][j] = dp[i][j-2]
                    elif p[j-2] == s[i-1] or p[j-2] == '.':
                        # if previous one match, then a* can be interpret as 0 time (dp[i][j-2]), 
                        # 1 time (dp[i][j-1]) or multiple times (dp[i-1][j]) 
                        dp[i][j] = dp[i-1][j] or dp[i][j-1] or dp[i][j-2]            
        if dp[-1][-1]:
            return True
        return False
            
            
            
                
                    
                
        
            
        
        