class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # binary search
        if not nums:
            return [-1, -1]
        
        lo, hi = 0, len(nums)-1
        # find left
        while lo < hi:
            mid = (hi + lo)//2
            # this will find minimum index such that >= target
            # [lo, hi)
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1
        left = lo
        
        if nums[left] != target:
            # early return if not found
            return [-1, -1]
       
        lo, hi = 0, len(nums)-1
        # find right
        while lo < hi:
            mid = (hi + lo)//2
            # this will find minimum index such that > target
            # [lo, hi)
            if nums[mid] > target:
                hi = mid
            else:
                lo = mid + 1
        # the result lo should be index such that > target, so lo-1 will be answer
        # when out of boundary, it also return len(nums)-1, so specially take care
        if nums[lo] == target:
            right = lo
        else:
            right = lo - 1
        
        return [left, right]
        
        
        
        