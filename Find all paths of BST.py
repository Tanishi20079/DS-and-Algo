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
    
# function to count paths or to count left nodes.
def count_paths(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    else:
        return count_paths(root.left)+count_paths(root.right)

n=int(input())
root=None
s=list(map(int,input().split()))
for i in s:
    root=insert(root,i)
print(count_paths(root))
