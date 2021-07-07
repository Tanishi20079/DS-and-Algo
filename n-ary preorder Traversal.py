"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result, stack = [], [root]
        while stack:
            node = stack.pop()
            if not node: continue
            result.append(node.val)
            stack += node.children[::-1]

        return result      
