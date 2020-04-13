class Solution:
    def getSkyline(self, buildings):
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
                        res.append([x, -hp[0]])
                else:
                    hp.remove(y)
                    heapq.heapify(hp)
        return res

solution = Solution()
print(solution.getSkyline([[6765,184288,53874],[13769,607194,451649],[43325,568099,982005],[47356,933141,123943],[59810,561434,119381],[75382,594625,738524],[111895,617442,587304],[143767,869128,471633],[195676,285251,107127],[218793,772827,229219],[316837,802148,899966],[329669,790525,416754],[364886,882642,535852],[368825,651379,6209],[382318,992082,300642],[397203,478094,436894],[436174,442141,612149],[502967,704582,918199],[503084,561197,625737],[533311,958802,705998],[565945,674881,149834],[615397,704261,746064],[624917,909316,831007],[788731,924868,633726],[791965,912123,438310]]))
                
                    
            
        
        
        
        

            
        
            
        