import copy
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # return copy.deepcopy(node)
        if not node:
            return node
        clone = {}
        queue = deque()

        # add node to the queue after being cloned so that its neighbors can be added
        clone[node] = Node(node.val)
        queue.append(node)
        while queue:
            next = queue.popleft()
            for n in next.neighbors:
                if n not in clone:
                # add node to the queue after being cloned so that its neighbors can be added
                    clone[n] = Node(n.val)
                    queue.append(n)
                # add the neighbors of next to its clone
                clone[next].neighbors.append(clone[n])
        return clone[node]

            
