class Solution:
    def jump(self, nums: List[int]) -> int:
        # greedy (BFS) idea
        # very trciky
        # for a list, we split them into different zones
        # each zone represent use i step, where is the furthest position we can reach
        # when we reach there, we are in i+1 step zone
        # until we reach the end
        
        if len(nums) == 1:
            return 0
        steps = 0
        cur_end, furthest = 0, 0
        
        for i in range(len(nums)):
            furthest = max(furthest, i + nums[i]) 
            
            if furthest >= len(nums)-1:
                steps += 1
                break
                
            if i == cur_end:
                steps += 1
                cur_end = furthest
            
        return steps
                
                    
                
            
            