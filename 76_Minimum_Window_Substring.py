class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # two pointers
        
        # Initial submission
        if not t or not s or len(s) < len(t):
            return ""
        
        cur_eff = dict() # record current effective letter number
        needs = dict() # record needed letter to make it quick to look-up
        locations = []
        res = ""
        
        for c in t:
            if c not in needs:
                needs[c] = 1
            else:
                needs[c] += 1
        
        # initial:
        left, right = None, None
        for i,c in enumerate(s):
            if c in needs:
                left, right = i, i
                break
        if left is None:
            return ""
        
                
        while right < len(s):
            c = s[right]
            
            if c in needs:
                cur_eff[c] = 1 if c not in cur_eff else cur_eff[c] + 1
                locations.append(right)
            
            # check if we get full set
            flag = 0
            while len(cur_eff.keys()) == len(needs.keys()):
                # detail check numbers of item is >= 
                for k, v in cur_eff.items():
                    if v < needs[k]:
                        flag = 1
                        break
                if flag == 1:
                    break
                
                if res == "" or len(res) > right-left:
                    res = s[left:right+1]

                # remove the first element in cur_eff
                cur_eff[s[left]] -= 1
                if cur_eff[s[left]] == 0:
                    del cur_eff[s[left]]
                # remove from location and update left
                locations.pop(0)
                if not locations:
                    return res
                left = locations[0]
                
            right += 1
                    
         
        return res


        # ############# Improvement
        # Slightly improvement by only using needed dictionary and keep a counting on the number of missing letters
        if not t or not s or len(s) < len(t):
            return ""
        
        needs = dict() # record needed letter to make it quick to look-up
        locations = []
        missing = len(t) # number of missing letters
        res = ""
        
        needs = Counter(t)
        
        # initial:
        left, right = None, None
        for i,c in enumerate(s):
            if c in needs:
                left, right = i, i
                break
        if left is None:
            return ""
        
                
        while right < len(s):
            c = s[right]
            
            if c in needs:
                if needs[c] > 0:
                    # only update missing for really needs letters
                    missing -= 1
                needs[c] -= 1
                locations.append(right)
            
            # check if we get full set
            while (missing == 0):
                if res == "" or len(res) > right-left:
                    res = s[left:right+1]

                # remove the first element 
                if needs[s[left]] == 0:
                    # only update missing when removing first would make a difference
                    missing += 1
                needs[s[left]] += 1
                # remove from location and update left
                locations.pop(0)
                if not locations:
                    return res
                left = locations[0]
                
            right += 1
                    
         
        return res
                
                
                
                
                
            
                
        