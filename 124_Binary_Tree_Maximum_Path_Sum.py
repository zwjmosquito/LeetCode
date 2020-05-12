# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # for each node, record - left_max (must include itself), right_max (must include itself)
        self.cur_max = -float('inf')
        
        def node_max(node):
            if not node.left and not node.right:
                self.cur_max = max(self.cur_max, node.val)
                return node.val
            
            if not node.left:
                left_max = node.val
            else:
                left_max = max(node.val, node_max(node.left) + node.val)
                
            if not node.right:
                right_max = node.val
            else:
                right_max = max(node.val, node_max(node.right) + node.val)

            self.cur_max = max(self.cur_max, left_max, right_max, 
                               left_max + right_max - node.val)
            
            return max(left_max, right_max)

        _ = node_max(root)
        
        return self.cur_max
        
        