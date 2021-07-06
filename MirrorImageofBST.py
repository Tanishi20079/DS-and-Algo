class Node:
    def __init__(self,val):
        self.key=val
        self.right=None
        self.left=None
        
def insert(root, val):
    if root is None:
        root=Node(val)
        return root
    if root.key>val:
        root.left=insert(root.left,val)
    else:
        root.right=insert(root.right,val)
    return root

def mirror_image(root):
    if root:
        temp=root.left
        root.left=root.right
        root.right=temp
        mirror_image(root.left)
        mirror_image(root.right)
    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key,end=" ")
        inorder(root.right)


n=int(input())
root=None
s=list(map(int,input().split()))
for i in s:
    root=insert(root,i)
mirror_image(root)
inorder(root)
