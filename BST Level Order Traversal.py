import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def height(self,root):
        if root is None:
            return -1
        return max(self.height(root.left),self.height(root.right))+1
      
    def levelOrder(self,root):
        for i in range(self.height(root)+1):
            printTree(root,i)

def printTree(root,level):
    if root:
        if level==0:
            print(root.data,end=' ')
        else:
            printTree(root.left,level-1)
            printTree(root.right,level-1)
            
            
        

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
