class node:
     def __init__(self,data):
         self.data=data
         self.nex=None
class single_linkedlist:
     def __init__(self):
         self.start=None
     def insert_last(self,data):
         newnode=node(data)
         if(self.start==None):
             self.start=newnode
         else:
             temp=self.start
             while(temp.nex is not None):
                 temp=temp.nex
             temp.nex=newnode
     def delete_first(self):
         if(self.start is None):
             print("Empty")
         else:
             #temp=self.start
             self.start=self.start.nex
     def traverse(self):
         if(self.start is None):
             print("Empty")
         else:
             temp=self.start
             while(temp is not None):
                 print(temp.data)
                 temp=temp.nex
     def reverse(self): 
        p=None
        curr=self.start 
        while(curr is not None): 
            q=curr.nex
            curr.nex=p 
            p=curr 
            curr=q
        self.start=p
        
linked=single_linkedlist()
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
#linked.delete_first()
#print("DEleted list\n")
#linked.traverse()
print("REversed linked list:\n")
linked.reverse()
linked.traverse()
    
    
    
    
   
