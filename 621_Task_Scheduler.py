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
        
            