class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        # trick problem
        # possible answer can be only be within r or r + 1 (like the example case)
        # for i > r + 1, it purely repeat
        # for i < r: not possible to find B to be a substring
        from math import ceil
        
        r = ceil(len(B)/len(A))
        for i in [r, r + 1]:
            if B in A*i:
                return i
        return -1
        