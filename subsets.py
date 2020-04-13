def subsets(nums):
    # DFS
    if not nums:
        return None
    
    res = []
    
    def getN(n, s, cur):
        if len(cur) == n:
            res.append(cur.copy())
            return                
        for i in range(s, len(nums)):
            cur.append(nums[i])
            getN(n, i+1, cur)
            cur.pop(-1)
        
    for n in range(len(nums) + 1):
        getN(n, 0, [])

    return res


print(subsets([1,2,3]))