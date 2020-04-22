class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # three pointers, red, cur, blue
        # red pointer is to make sure all the color before it is red
        # blue pointer is to make sure all the color after is is blue
        
        if not nums:
            return []
        
        red, cur, blue = 0, 0, len(nums)-1
        
        while cur <= blue:
            if nums[cur] == 0:
                nums[cur], nums[red] = nums[red], nums[cur]
                red += 1
                # the reason we need to add one to cur is because swap with red, only means swap with a 1 (otherwise red == cur and we can still move to next)
                # swap with 1 is equivalent to cur + 1 (the else case) 
                cur += 1
            elif nums[cur] == 2:
                nums[cur], nums[blue] = nums[blue], nums[cur]
                blue -= 1
            else:
                cur += 1
                
        