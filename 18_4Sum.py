class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # use a record to save two sum
        record = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] in record:
                    record[nums[i] + nums[j]].append((i, j))
                else:
                    record[nums[i] + nums[j]] = [(i, j)]
        result = set()
        for s, pairs in record.items():
            if target - s not in record:
                continue
            psb_pairs = record[target - s]
            for i, j in pairs:
                for psb_i, psb_j in psb_pairs:
                    if psb_i == i or psb_j == j or psb_i == j or psb_j == i:
                        continue
                    res = sorted([nums[i], nums[j], nums[psb_i], nums[psb_j]])
                    result.add(tuple(res))
        return list(result)
        