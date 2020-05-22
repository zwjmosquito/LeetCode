class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0
        
        last_sum = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        for num in nums[1:]:
            cur_step = {}
            for t in list(last_sum.keys()):
            # here, we don't care how many times has t + num in last_sum, because with the current num, it can not be t + num again
            # but it possible that we already get a t + num in cur_step, so we need to add that into account
                cur_step[t + num] = cur_step.get(t + num, 0) + last_sum.get(t, 0)
                cur_step[t - num] = cur_step.get(t - num, 0) + last_sum.get(t, 0)
            last_sum = cur_step
        return last_sum.get(S, 0)
                    
        