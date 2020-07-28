class node:
     def __init__(self,value):
         self.value=value
         self.left=None
         self.right=None
#insert element
     def insert(self,value): 
         if(self):
             if(value>self.value):
                 if(self.right is None):
                     self.right=node(value)
                 else:
                     self.right.insert(value)
             elif(value<self.value):
                 if(self.left is None):
                     self.left=node(value)
                 else:
                     self.left.insert(value)
         else:
             self.value=value
#traversing using recursion
     def inorder(self,root):
         res=[]
         if root:
             res=self.inorder(root.left)
             res.append(root.value)
             res=res+self.inorder(root.right)
             
         return res
     def postorder(self,root):
         res=[]
         if root:
             res=self.inorder(root.left)
             res=res+self.inorder(root.right)
             res.append(root.value)
         return res
     def preorder(self,root):
         res=[]
         if self:
             
             res.append(self.value)
             res=res+self.inorder(self.left)
             res=res+self.inorder(self.right)
         return res
#searching a key
     def search_key(self,key):
         if(key<self.value):
             if(self.left is  None):
                 print("No found"+str(key))
             else:
                 (self.left.search_key(key))
         elif(key>self.value):
             if(self.right is   None):
                 print("Not found"+str(key))
             else:
                 (self.right.search_key(key))
         else:
             print("Found"+str(key))
#minimum value retrive
     def minvalue(self,root):
         self.root=root
         while(root.left is not None):
           root=root.left
         return root
#delete an element from the tree
     def delete(self,key):
         if(self is None):
             return None
         elif(self.value>key):
             return self.left.delete(key)
         elif(self.value<key):
             return self.right.delete(key)
         else:
             if(self.left is None):
                 temp=self.right
                 self=None
                 return temp
             elif(self.right is None):
                 temp=self.left
                 self=None
                 return temp
             else:
                 temp=self.right.minvalue(self.right)
                 self.value=temp.value
                 self.right.delete(temp.value)
         return self
# traverse using iteration
     def inorder_it(self,root):
         self.root=root
         res=[]
         curr=root
         while(curr or res):
             if(curr):
                 res.append(curr)
                 curr=curr.left
             else:
                 curr=res.pop()
                 print(curr.value)
                 curr=curr.right
  
root=node(50)
root.insert(30)
root.insert(20)
root.insert(60)
root.insert(70)
root.insert(80)
root.insert(40)
root.insert(55)
print("Inorder Traversal in recursive way:\n")
print(root.inorder(root))
print("Preorder Traversal in recursive way:\n")
print(root.preorder(root))
print("Postorder Traversal in recursive way:\n")
print(root.postorder(root))
root.search_key(20)
root.search_key(100)
print("After Deletion:\n")
root.delete(60)
print(root.inorder(root))
#root.minvalue(root)
print("Inorder Traversal iterative way:\n")
print(root.inorder_it(root))
