li=[]
class Node:
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None

def insert(root, key):
    if root is None:
        root=Node(key)
        return root
    if root.key>key:
        root.left=insert(root.left,key)
    else:
        root.right=insert(root.right,key)
    return root

def inorder(root):
    global li
    if root:
        inorder(root.left)
        li.append(root.key)
        inorder(root.right)

n=int(input())
li=[]
s=list(map(int,input().split()))
root=None
for i in s:
    root=insert(root,i)
inorder(root)
if len(li)%2==1:
    print(li[len(li)//2])
else:
    print((li[len(li)//2]+li[len(li)])/2)
