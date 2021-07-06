class Node:
    def __init__(self,val):
        self.key=val
        self.left=None
        self.right=None
        self.parent=None

def insert(root, val,parent):
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
    return max(height(root.left),height(root.right))+1
    
def print_zig_zag(root,level,i):
    if root:
        if level==i:
            print(root.key,end=" ")
        elif level>i:
            if level%2==0:
                print_zig_zag(root.right, level,i+1)
                print_zig_zag(root.left, level, i+1)
            else:
                print_zig_zag(root.left,level,i+1)
                print_zig_zag(root.right,level,i+1)
                
                
n=int(input())
l=list(map(int,input().split()))
root=None
for i in l:
    root=insert(root,i, None)
for i in range(height(root)+1):
    print_zig_zag(root,i,0)
                
        
