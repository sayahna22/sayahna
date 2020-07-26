class node:
     def __init__(self,data):
         self.data=data
         self.prev=None
         self.next=None
class double_linkedlist:
     def __init__(self):
         self.start=None
     def insert_last(self,data):
         newnode=node(data)
         if(self.start is None):
             self.start=newnode
         else:
             temp=self.start
             while(temp.next is not  None):
                 temp=temp.next
             temp.next=newnode
             newnode.prev=temp
             
     def traverse(self):
         if(self.start==None):
             print("Empty")
         else:
             temp=self.start
             while(temp is not None):
                 print(temp.data)
                 temp=temp.next
     def reverse(self):
         temp=self.start
         while(temp is not None):
             p=temp
             temp=temp.next
         while(p is not None):
             print(p.data)
             p=p.prev
     
     
    
linked=double_linkedlist()
linked.insert_last(1)
linked.insert_last(2)
linked.insert_last(3)
linked.insert_last(4)
linked.insert_last(5)
linked.insert_last(6)
linked.insert_last(7)
print("INPUTS are:\n")
linked.traverse()
print("\n")
print("Reversed linked list:\n")
linked.reverse()
print("\n")

#linked.delete_first()
#print("DEleted list\n")
#linked.traverse()
    
