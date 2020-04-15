class Solution:
    def getSkyline(self, buildings):
        """
        Idea is maintain a priority queue on the current height, each time when seeing a new start point, push it to the queue. Otherwise, remove from the queue. If the push or remove operations has changed the highest height, then it will be a critical point that we want to record
        Note: some edge cases on same x, same y, and 'b', 'e' on the same x etc. that's why the xyf need to be specially sorted 
        """
        import heapq
        
        if not buildings:
            return []
        
        # step 1: from buildings to a sorted list
        xyf = [[l, -h, 'b'] for l, r, h in buildings] + [[r, -h, 'e'] for l, r, h in buildings] 
        # sort xyf
        xyf = sorted(xyf, key = lambda x: (x[0], x[2], -x[1]) if x[2] == 'e' else (x[0], x[2], x[1]))
        
        hp = [0]
        res = []

        for (x, y, f) in xyf:            
            cur_min = hp[0]
            if f == 'b':
                heapq.heappush(hp, y)
                after_min = hp[0]
                if after_min != cur_min:
                    res.append([x, -y])
            else:
                if y == cur_min:
                    heapq.heappop(hp)
                    if y != hp[0]:
                        # if is for special case hp has two max values
                        res.append([x, -hp[0]])
                else:
                    hp.remove(y)
                    # here is where the improvement can be done
                    heapq.heapify(hp)
        return res

solution = Solution()
testcase = []
print(solution.getSkyline(testcase))
                
                    
            
        
        
        
        

            
        
            
        