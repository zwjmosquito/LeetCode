# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # recursive
        if not root:
            return True
        
        def helper(node, lb, ub):
            if not node:
                return True
            if node.val >= ub or node.val <= lb:
                return False
            
            left, right = True, True
            if node.left:
                # for left subtree, it must less than current node.val
                # but it also has lower bound requirement from last layer
                left = helper(node.left, lb, node.val)
            if node.right:
                # similar for right tree
                right = helper(node.right, node.val, ub)
        
            return left and right
        
        return helper(root, -float(inf), float(inf))
            
        