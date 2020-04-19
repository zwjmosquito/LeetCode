class Solution:
    from typing import List
    def canPartition(self, nums: List[int]) -> bool:
        # The idea of first solution is to build a hashmap record what's needed to get target 
        if not nums:
            return False
        # first check for sum
        if sum(nums)%2 == 1:
            return False
        
        target = sum(nums)/2
        need = {target: 1}
        
        # when iterate over the list, everytime we will update the need keys
        for i in nums:
            if i in need:
                return True
            if i > target:
                return False

            # to avoid change dictionary size during iteration, make a copy
            past_keys = list(need.keys())
            for k in past_keys:
                # update need to each existing keys
                if k-i > 0: 
                    need[k-i] = 1
        
        return False


        # Then I reviewed backpack problem and come up with dp solution below
        if not nums:
            return False
        # first check for sum
        if sum(nums)%2 == 1:
            return False
        
        target = int(sum(nums)/2)
        
        # dp[i][j] represent use first i item get sum j's possibility (1, 0)
        # dp = [[0 for _ in range(target+1)] for _ in range(len(nums) + 1)]
        # **************** #
        # however, the only need thing is only the location of 1 in previous layer, we don't need to 
        # iterate over the whole dp list
        # Therefore I change the code to only recording the locations. which turns out to be the same idea 
        # as Method I
        loc = set([0])
        
        for i in range(1, len(nums) + 1):
            tmp_loc = set()
            if nums[i-1] > target:
                return False
            if nums[i-1] == target:
                return True
            
            tmp_loc.add(nums[i-1])

            for j in loc:
                if (j+nums[i-1]) < target+1:
                    # update current loc to be 1 based on previous loc
                    tmp_loc.add(j+nums[i-1])
                # this is the case when not adding num[i-1]
                tmp_loc.add(j)
            loc = tmp_loc
            
            if target in loc:
                return True
        return False

slt = Solution()
inpu = [1,2,3,4,5,6,7]
slt.canPartition(inpu)            
            
            
        
        
            
        
            
            
            
        
        
            
        