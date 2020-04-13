def permu(nums):
    if not nums:
        return []
    res = []

    def comb(cur, rest):
        if len(cur) == len(nums):
            res.append(cur)
            return

        for j in range(len(rest)):
            tmp_rest = rest[j:] + rest[:j]
            cur.append(tmp_rest[0])
            tmp_rest.pop(0)
            comb(cur, tmp_rest)
            cur.pop(-1)

    # iterate over start nums
    for idx in range(len(nums)):
        comb([nums[idx]], nums[:idx] + nums[idx+1:])
    return res

print(permu([1,3,5]))