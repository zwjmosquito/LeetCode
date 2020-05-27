class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        record = {} 
        res = 1
        
        for num in nums:
            # store length of sequence in the boundary point
            if num in record:
                continue
            
            l, r = record.get(num - 1, 0), record.get(num + 1, 0)
            length = l + r + 1
            # store at left point
            record[num] = length
            record[num - l] = length
            record[num + r] = length
            res = max(res, length)
        
        return res 
                
        ## brute force method
        # easily see how we get the optimal solution from brute force
        # since every time, we need to find left and right boundary and update res
        # the idea of store length in l, r boundary is the key, it's tricky
        if len(nums) <= 1:
            return len(nums)
        
        record = {} 
        res = 1
        
        for num in nums:
            l, r = num, num
            record[num] = 1
            while r in record:
                r += 1
            while l in record:
                l -= 1
            res = max(res, r - l - 1)
        
        return res 