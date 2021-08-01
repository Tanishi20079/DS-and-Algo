# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return isMirror(root,root)

def isMirror(t1,t2):
    if t1 is None and t2 is None:return True
    if t1 is None or t2 is None: return False
    return (t1.val==t2.val) and isMirror(t1.left,t2.right) and isMirror(t1.right,t2.left)
