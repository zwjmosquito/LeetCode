class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # brute-force - use a dictionary to record frequency
        if not s or len(s) < len(p):
            return []
        
        anagram = {}
        n = len(p)
        all_list = list(map(chr, range(ord('a'), ord('z')+1)))
        counter = {l: 0 for l in all_list}
        for c in p:
            counter[c] += 1
            
        res = []
        cur_counter = {l: 0 for l in all_list}
            
        for i in range(len(s) - n + 1):
            if i == 0:
                for c in s[:n]:
                    cur_counter[c] += 1
            else:
                cur_counter[s[i-1]] -= 1
                cur_counter[s[i+n-1]] += 1   
            if cur_counter == counter:
                res.append(i)
        
        return res
                
        