class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # two list record: pre[i] = prod(0,...i-1), post[i] = prod(i+1,...)
        if not nums:
            return []
        if len(nums) == 1:
            return [0]
        
        pre, post = [1]*len(nums), [1]*len(nums)
        
        for i in range(1, len(nums)):
            pre[i] = pre[i-1]*nums[i-1]
            post[len(nums)-i-1] = post[len(nums)-i]*nums[len(nums)-i]
        
        return [pre[i]*post[i] for i in range(len(nums))]
        
        
        # method 2: just combine the above operation together and record the result in one list
        result = []
        p = 1
        for i in range(len(nums)):
            result.append(p)
            p = p*nums[i]
        p = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] = result[i]*p
            p = p*nums[i]
        
        return result