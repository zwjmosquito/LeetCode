class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i] - max subarray ending with i
        if not nums:
            return 0
        
        # dp[i] = max(dp[i-1] + nums[i], nums[i])
        # no need to keep dp array, just need a prev_sum
        cur_max, prev_sum = nums[0], nums[0]
        for i in range(1, len(nums)):
            prev_sum = max(nums[i], prev_sum + nums[i])
            cur_max = max(cur_max, prev_sum)
        return cur_max
            
        