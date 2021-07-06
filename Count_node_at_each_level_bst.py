class Node:
    def __init__(self,val):
        self.key=val
        self.parent=None
        self.left=None
        self.right=None
    
def insert(root, val, parent):
    if root is None:
        root=Node(val)
        root.parent=parent
        return root
    if root.key>val:
        root.left=insert(root.left,val,root)
    else:
        root.right=insert(root.right,val,root)
    return root

def height(root):
    if root is None:
        return -1
    return 1+max(height(root.left),height(root.right))

def countLevel(root,level):
    if root:
        if level==0:
            return 1
        else:
            if level:
                return countLevel(root.left, level-1)+countLevel(root.right,level-1)
            else:
                return 0
    return 0
    
    
n=int(input())
s=list(map(int,input().split()))
root=None
for i in s:
    root=insert(root,i,None)
for i in range(height(root)+1):
    print('Nodes at Level',i,'=',countLevel(root,i))
        
        
        
