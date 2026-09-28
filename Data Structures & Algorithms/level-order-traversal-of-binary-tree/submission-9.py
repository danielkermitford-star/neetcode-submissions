# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
   def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    dfs_list_of_levels = []
    node_queue = deque()

    cur_level = 0
    nodes_at_cur_level = []
    node_queue.appendleft((root, 0))
    while node_queue:
        node, level = node_queue.pop()
        if node:
            # print(node.val)
            node_queue.appendleft((node.left, level + 1))
            node_queue.appendleft((node.right, level + 1))

            if level > cur_level:
                dfs_list_of_levels.append(nodes_at_cur_level)
                nodes_at_cur_level = []
                cur_level = level
            nodes_at_cur_level.append(node.val)

    if nodes_at_cur_level:
        dfs_list_of_levels.append(nodes_at_cur_level)
    return dfs_list_of_levels

            

        