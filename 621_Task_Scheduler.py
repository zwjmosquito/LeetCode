class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        ### arrange most frequent first
        ### if there are more than one most frequent
        ### insert the rest after (+ max_count_tasks)
        ### then the rest of most frequent can be treated as less frequent one
        ### so we can use the same formula to calculate - (max_count - 1)*(n + 1)
        
        tasks_count = list(Counter(tasks).values())
        max_count = max(tasks_count)
        max_count_tasks = tasks_count.count(max_count)
        

        return max(len(tasks), (max_count - 1)*(n + 1) + max_count_tasks)
        

        # Second Method 
        from collections import Counter
        from heapq import heappush, heappop
        # use a heap to store frequency of left letters
        # python has min heap - use negative
        counter = Counter(tasks)
        heap = []
        for k, v in counter.items():
            heappush(heap, (-v, k))
        
        cur_time = 0
        while heap:
            temp = {}
            for i in range(n+1):
                cur_time += 1
                # pop
                if heap:
                    v, k = heappop(heap)
                    # if only one left
                    if v != -1:
                        temp[k] = v + 1
                if not heap and not temp:
                    break

            for k, v in temp.items():
                heappush(heap, (v, k))
                

        return cur_time
        
                