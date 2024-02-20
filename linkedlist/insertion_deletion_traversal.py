class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None
    
    def insertion_at_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        
    
    def insertion_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            new_node.next=self.head.next
            self.head=new_node
            return
        tmp=self.head
        while tmp.next:
            tmp=tmp.next
        tmp.next=new_node
        
    def traversal(self):
        tmp=self.head
        while tmp:
            print(str(tmp.data)+" ->",end=' ')
            tmp=tmp.next
        print("\n")
    
    def delete_element(self,val):
        if self.head is None:
            print("Empty list")
            return
        tmp=self.head
        while tmp.next:
            tmp=tmp.next
            if tmp.next.data==val:
                break
            
        if tmp is None:
            print("element not present")
            return
        prev=tmp
        tmp=tmp.next
        prev.next=tmp.next
        tmp=None
        
        
        

l=LinkedList()
ll=[1,2,3,4,5,6]
for i in range(0,len(ll)-1,2):
    l.insertion_at_begin(ll[i])
    l.insertion_at_end(ll[i+1])
l.traversal()
l.delete_element(6)
l.traversal()

            
