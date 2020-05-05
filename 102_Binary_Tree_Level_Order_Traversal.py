# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # BFS
        if not root:
            return []
        res = []
        cur = [root]
        
        while cur:
            res.append([])
            tmp_cur = []
            for item in cur:
                if item.left: 
                    tmp_cur.append(item.left)
                if item.right:
                    tmp_cur.append(item.right)
                res[-1].append(item.val)
            cur = tmp_cur
        return res
                
        
        