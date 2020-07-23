class Node:
     def __init__(self,data):
         self.l=None
         self.r=None
         self.data=data
     #insert the elements to the tree
     def insert(self,data):
         if(self.data):
             if(self.data<data):
                 if(self.r is None):
                     self.r=Node(data)
                 else:
                     self.r.insert(data)
             elif(self.data>data):
                 if(self.l is None):
                     self.l=Node(data)
                 else:
                     self.l.insert(data)
         else:
             self.data=data
     # search an element
     def search_key(self,val):
         if(val<self.data):
             if(self.l is None):
                 return(str(val)+"NOT FOUND")
             return self.l.search_key(val)
         elif(val>self.data):
             if(self.r is None):
                 return(str(val)+"NOT FOUND")
             return self.r.search_key(val)
         else:
             print(str(self.data)+"FOUND")
     def print_tree(self):
         if(self.l):
             self.l.print_tree()
             print(self.data)
         if(self.r):
             self.r.print_tree()
'''
ele=int(input("Enter the root value:"))
root=Node(ele)
num=int(input("Enter the array size:"))
for i in range(num):
     s=int(input())
     root.insert(s)
root.print_tree()
'''
root=Node(10)
root.insert(4)
root.insert(7)
root.insert(9)
print(root.search_key(3))
print(root.search_key(7))







   
   

