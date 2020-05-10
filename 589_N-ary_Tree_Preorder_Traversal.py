"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # iterative way
        if not root:
            return []
        stack, res = [root], []
        while stack:
            node = stack.pop()
            res.append(node.val)
            for child in node.children[::-1]:
                stack.append(child)
        return res

        # recursive
        if not root:
            return []
        res = []
        for node in root.children:
            res += self.preorder(node)
        
        return [root.val] + res
                
                
        