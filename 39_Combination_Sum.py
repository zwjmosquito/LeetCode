class Solution:
    frim typing import List
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # initial thought: dfs 
        # My first attemp: Time Limit Exceed - reason is I didn't track index in dfs
        # Even though it can repeatedly use one number, it doesn't need to go "backwards"
        # for example, [3,2,8], the combination 3,3,2 should be go through when starting from 3
        # in the recursion starting from 2, there is no need to go through 2,3,2 again

        # In the current implementation, sort candidates can make early break (which improve the run time)
        # cur_res + [candidates[i]] makes a copy, so there is no need to append(cur_res.copy())
        
        if not candidates:
            return []
        
        res = []
        candidates.sort()
        
        def dfs(cur_sum, cur_res, index):            
            if cur_sum == target:
                res.append(cur_res)
                return
            for i in range(index, len(candidates)):
                if cur_sum + candidates[i] > target:
                    break
                dfs(cur_sum + candidates[i], cur_res + [candidates[i]], i)        
        dfs(0, [], 0)
        return res


        ## Below is the dp solution
        # dp[i] = comb_res, combination list that can add up to i
        
        if not candidates:
            return []
        
        res = []
        dp = [[] for _ in range(target+1)]
        
        for i in range(target+1):
            for num in candidates:
                if num > i:
                    continue
                if num == i:
                    dp[i].append([num])
                
                for item in dp[i-num]:
                    tmp_item = item + [num]
                    tmp_item.sort()
                    if tmp_item not in dp[i]:
                        dp[i].append(tmp_item)
        
        res = dp[target]
                            
        return res
        
        

slt = Solution()
input1 = [92,71,89,74,102,91,70,119,86,116,114,106,80,81,115,99,117,93,76,77,111,110,75,104,95,112,94,73]
input2 = 310

res = slt.combinationSum(candidates=input1, target=input2)
print("*"*30)
print(res)
        