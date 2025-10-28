"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        newGraph = {}
        queue = deque([node])
        newGraph[node] = Node(node.val)

        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                if neighbor not in newGraph:
                    newGraph[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                newGraph[curr].neighbors.append(newGraph[neighbor])
        
        return newGraph[node]