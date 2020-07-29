class node:
     def __init__(self,data):
         self.data=data
         self.right=None
         
class  single_linkedlist:
     def __init__(self):
         self.root=None
#insert element at the last
     def insert_last(self,data):
         newnode=node(data)
         if(self.root==None):
             self.root=newnode
         else:
             temp=self.root
             while(temp.right is not None):
                 temp=temp.right
             temp.right=newnode
#traverse the linkedlist
     def traverse(self):
         if(self.root is None):
             print("Empty")
         else:
             temp=self.root
             while(temp is not None):
                 print(temp.data)
                 temp=temp.right
#detect a loop
     def find_a_loop(self):
         p=self.root
         q=self.root
         while(p and q and q.right ):
              p=p.right
              q=q.right.right
              if(p==q):
                 print("Found")
                 break
             
              
#insert at any position
     def insert_atany_pos(self,data,pos):
         newnode=node(data)
         if(pos is None):
             print("Wrong")
         else:
             temp=pos.right
             pos.right=newnode
             newnode.right=temp
         
#delete the first node
     def delete_first(self):
         if(self.root is None):
             print("Empty")
         else:
             self.root=self.root.right

#delete the given prev_pos node
     def delete_at_any_pos(self,pos):
         if(self.root is None):
             print("Empty")
         else:
             temp=pos.right
             pos.right=temp.right

 #reverse a single linked list
     def reverse_linked_list(self):
         prev=None
         curr=self.root
         while (curr is not None):
             q=curr.right
             curr.right=prev
             prev=curr
             curr=q
         self.root=prev
                 
lis=single_linkedlist()
lis.insert_last(2)
lis.insert_last(4)
lis.insert_last(5)
lis.insert_last(1)
lis.insert_last(6)
print("Traversa of the single linked list")
print(lis.traverse())
lis.root.right.right=lis.root
(lis.find_a_loop())
lis.insert_atany_pos(45,lis.root.right)
print("Insert at any pos traversal:")
print(lis.traverse())
lis.delete_first()
print("After deleting the first node:")
print(lis.traverse())
lis.delete_at_any_pos(lis.root.right)
print("After deleting the  node:")
print(lis.traverse())
lis.reverse_linked_list()
print("The reversed linked_list:")
print(lis.traverse())


 
