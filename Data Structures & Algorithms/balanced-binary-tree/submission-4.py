# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def db(self, root: Optional[TreeNode]) -> (int, int):
        if not root:
            return (0, True)
        l_depth, l_balanced = self.db(root.left)
        r_depth, r_balanced = self.db(root.right)
    
        balanced = l_balanced and r_balanced and abs(l_depth-r_depth) <= 1
        return (1+max(l_depth, r_depth), balanced)
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.db(root)[1]
