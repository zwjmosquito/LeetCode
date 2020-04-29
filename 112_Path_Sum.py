# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # recursion
        if not root:
            return False
        if not root.left and not root.right:
            return False if root.val != sum else True 
        
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

        # BFS
        if not root:
            return False
        
        cur_layer, cur_sum = [root], [root.val]
        while cur_layer:
            tmp_l, tmp_s = [], []
            
            for n, s in zip(cur_layer, cur_sum):
                if n.left: 
                    tmp_l.append(n.left)
                    tmp_s.append(s + n.left.val)
                if n.right:
                    tmp_l.append(n.right)
                    tmp_s.append(s + n.right.val)
                
                if not n.left and not n.right and s == sum:
                    return True
                
            cur_layer = tmp_l
            if tmp_l: 
                cur_sum = tmp_s

        if sum in cur_sum:
            return True
        
        return False
        

        # DFS 
        if not root:
            return False
        
        self.res = False
        
        def DFS(node, cur_sum):
            if not node:
                return
            
            cur_sum += node.val
            
            if not node.left and not node.right and cur_sum == sum:
                self.res = True
                return
            
            DFS(node.left, cur_sum)
            DFS(node.right, cur_sum)
        
        DFS(root, 0)
        return self.res