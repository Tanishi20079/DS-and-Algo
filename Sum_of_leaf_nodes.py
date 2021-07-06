class Node:
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.root=None
    def insert(self, root, key):
        if root is None:
            root=Node(key)
            return root
        if root.key>key:
            root.left=self.insert(root.left,key)
        else:
            root.right=self.insert(root.right,key)
        return root
def getleafsum(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.key
    return getleafsum(root.left)+getleafsum(root.right)

for _ in range(int(input())):
    n=int(input())
    li=[]
    s=list(map(int,input().split()))
    mytree=Tree()
    for i in s:
        mytree.root=mytree.insert(mytree.root,i)
    print(getleafsum(mytree.root))
