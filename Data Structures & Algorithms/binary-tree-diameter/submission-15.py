# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dd(self, root: Optional[TreeNode]) -> (int, int):
        if not root:
            return (-1,-1)
        l_depth, l_dia = self.dd(root.left)
        r_depth, r_dia = self.dd(root.right)
        
        return (1+ max(l_depth, r_depth), max(l_dia, r_dia, 2 + l_depth + r_depth))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        depth, dia = self.dd(root)
        return max(0, depth, dia)


        