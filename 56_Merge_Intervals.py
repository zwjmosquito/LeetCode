class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        sorted_list = sorted(intervals, key=lambda i: i[0])
        res = [sorted_list[0]]
        for i in range(1, len(sorted_list)):
            # check overlap between res and current interval
            # if overlap
            if res[-1][1] >= sorted_list[i][0]:
                latest_start, latest_end = res.pop(-1)
                res.append([latest_start, max(sorted_list[i][1], latest_end)])
            # no overlap
            else:
                res.append(sorted_list[i])
        return res
