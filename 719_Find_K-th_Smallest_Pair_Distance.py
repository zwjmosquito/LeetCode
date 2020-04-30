class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # dp + binary search
        # dp[i]: how many pairs can be constructed with nums[:i] (left) + rest (right)
        # s.t. distance between them <= value
        # dp[n-1] will be total #
        # if dp[n-1] < k: value is small, search for RHS
        # if dp[n-1] >= k: value is large, search on LHS
        
        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        N = len(nums)
        
        while l <= r:
            m = (r + l) // 2
            dp = [0]*N
            
            j = 0
            for i in range(N):
                while j < N and nums[j] - nums[i] <= m:
                    j += 1
                dp[i] = dp[i-1] + (j - i - 1) # j-i-1 is # of elements between them which represent how many pairs can be constructed

            if dp[N-2] < k:
                l = m + 1
            else:
                r = m - 1
        
        return l
            
                
                    
                
            
        