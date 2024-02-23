class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
def printLevelOrder(root):
    h=height(root)
    for i in range(1,h+1):
        curlevel(root,i)
    
def curlevel(root,h):
    if root is None:
        return
    if h==1:
        print(root.data)
    else:
        curlevel(root.left,h-1)
        curlevel(root.right,h-1)


def height(node):
    if node is None:
        return 0
    lh=height(node.left)
    rh=height(node.right)
    if lh>rh:
        return lh+1
    else:
        return rh+1
        

def getwidth(root):
    max_width=0
    h=height(root)
    print("height of tree",h)
    for i in range(1,h+1):
        width=calwidth(root,i)
        max_width=max(max_width,width)
    print("MAx width",max_width)

def calwidth(root,l):
    if root is None:
        return 0
    if l==1:
        return 1
    else:
        return calwidth(root.left,l-1)+calwidth(root.right,l-1)

root=Node(1)
root.left=Node(2)
root.left.left=Node(3)
root.left.right=Node(6)
root.right=Node(4)
root.right.left=Node(8)
root.left.left.left=Node(5)

printLevelOrder(root)
getwidth(root)
