class Node:
    def __init__(self,data):
        self.next=None
        self.data=data

class Linkedlist:
    def __init__(self):
        self.head=None
        
    def push_start(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
     
    def push_end(self,data):
        new_node=Node(data)
        if self.head is None:
            new_node.next=self.head
            self.head=new_node
            return
        tmp=self.head
        while tmp.next:
            tmp=tmp.next
        tmp.next=new_node
        
    
    def printhead(self):
        tmp=self.head
        while tmp:
            print(tmp.data,"-->",end="")
            tmp=tmp.next
    
        


l=Linkedlist()
l.push_end(1)
l.push_start(2)
l.push_end(3)
l.printhead()
        
