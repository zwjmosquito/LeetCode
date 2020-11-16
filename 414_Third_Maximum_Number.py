class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # maintain an increasing queue of size 3
        
        v = [-float(inf), -float(inf), -float(inf)]
        
        for num in nums:
            if num not in v:
                if num > v[2]:
                    v = [v[1], v[2], num]
                elif num > v[1]:
                    v = [v[1], num, v[2]]
                elif num > v[0]:
                    v = [num, v[1], v[2]]
        
        if -float(inf) in v:
            return max(v)
        return v[0]
        
        
        