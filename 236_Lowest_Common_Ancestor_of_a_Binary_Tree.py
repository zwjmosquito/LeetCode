# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Method I: Initial Idea
        # find a path from root to p and a path from root to q
        # find node in both path (farest from root)
        
        if not root:
            return None
        
        def find_node(node, target, path):
            if not node:
                return []
            if node == target:
                return path + [node]
            
            left_path = find_node(node.left, target, path + [node])
            right_path = find_node(node.right, target, path + [node])
            
            return left_path if left_path else right_path
 
        
        path_p = find_node(root, p, [])
        path_q = find_node(root, q, [])
        
        
        if len(path_p) > len(path_q):
            path_p, path_q = path_q, path_p
        
        for i in range(1, len(path_p) + 1):
            if path_p[-i] in path_q:
                return path_p[-i]
        
        
        # Method II: Important Way of thinking for tree problem - consider 
        # a single node and it's left subtree, right subtree
        # Runtime: 72 ms (Method I was 3448ms)
        # recursion use the function
        # if p or q is root:
        if root == p or root == q:
            return root
        
        left, right = None, None
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)
        
        # if find p, q in both left and right
        if left and right:
            return root
        # if only find in on part, then that part should have returned the LCA
        if left or right:
            return left if left else right
        return None
            
            
        