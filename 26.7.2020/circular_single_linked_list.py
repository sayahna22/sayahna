class node:
     def __init__(self,data):
         self.data=data
         self.next=None
class circular_single:
     def __init__(self):
        self.start=None
     def insert(self,data):
         newnode=node(data)
         if(self.start==None):
             self.start=newnode
         else:
             temp=self.start
             while(temp.next is not None):
                 temp=temp.next
             temp.next=newnode
             newnode=self.start
     def traverse(self):
         if(self.start==None):
             print("Empty")
         else:
             temp=self.start
             while(temp is not None):
                 print(temp.data)
                 temp=temp.next
                 if(temp==self.start):
                      break
     def delete(self):
         if(self.start)==None:
             print("Empty")
         else:
             self.start=self.start.next
             
     
linked=circular_single()
linked.insert(1)
linked.insert(2)
linked.insert(3)
linked.insert(4)
linked.insert(5)
linked.insert(6)
linked.insert(7)
print("INPUTS are:\n")
linked.traverse()
linked.delete()
linked.traverse()

