class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # two pointer
        i, j = 0, 0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            else:
                if j == 0 or typed[j] != typed[j-1]:
                    return False
                if typed[j] == typed[j-1]:
                    j += 1
        if i < len(name):
            return False
        if len(typed[j:]) <= 1:
            return True
        return False
        