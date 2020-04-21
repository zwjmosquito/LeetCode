# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # preorder: [root, (left), (right)]
        # inorder:  [(left), root, (right)]
        # key: find (left) and (right)
        
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        ind = inorder.index(root.val)
        
        root.left = self.buildTree(preorder[1:ind+1], inorder[:ind])
        root.right = self.buildTree(preorder[ind+1:], inorder[ind+1:])
        
        return root

slt = Solution()
preorder = [1,2,3]
inorder = [3,2,1]
res = slt.buildTree(preorder, inorder)
print(res)