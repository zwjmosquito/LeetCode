class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # check number of isolated region - wrong: check number of overlap region
        # sort all pairs
        
        if not points:
            return 0
        points.sort()
        res = []
        
        for start, end in points:
            if not res or start > res[-1][1]:
                res.append([start, end])
            if res and start <= res[-1][1]:
                prev_start, prev_end = res.pop()
                end = min(prev_end, end)
                res.append([start, end])

        return len(res)
            
            
        