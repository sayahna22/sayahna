class node:
     def __init__(self,data):
         self.data=data
         self.link=None
class linked_list:
     def __init__(self):
         self.root=None
     def insert_last(self,data):
         new=node(data)
         if(self.root is None):
             self.root=new
         else:
             temp=self.root 
             while(temp.link is not None):
                 temp=temp.link
             temp.link=new
     def swap_node(self,a,b):
         if(self.root is None):
             print("Empty")
         else:
             x=None
             y=None
             if(a==b):
                 return None
             temp=self.root
             while(temp.link is not None ):
                 if(temp.link.data==a):
                     x=temp
                 elif(temp.link.data==b):
                     y=temp
                 temp=temp.link
             if(x is not None and y is not None):
                 t=x.link
                 x.link=y.link
                 y.link=t
                 t=x.link.link
                 x.link.link=y.link.link
                 y.link.link=t
                
     def traverse(self):
         if(self.root is None):
             print("Empty")
         else:
             temp=self.root
             while(temp is not None):
                 print(temp.data)
                 temp=temp.link
n=linked_list()
n.insert_last(1)
n.insert_last(2)
n.insert_last(3)
n.insert_last(4)
n.insert_last(5)
n.insert_last(6)
print("Before Swapping")
n.traverse()
n.swap_node(4,3)
print("After Swapping")
n.traverse()


