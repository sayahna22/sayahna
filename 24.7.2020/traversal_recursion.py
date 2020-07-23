class Node:
     def __init__(self,data):
         self.left=None
         self.right=None
         self.data=data
     def insert(self,data):
         if(self.data):
             if(self.data>data):
                 if(self.left is None):
                     self.left=Node(data)
                 else:
                     self.left.insert(data)
             elif(self.data<data):
                 if(self.right is None):
                     self.right=Node(data)
                 else:
                     self.right.insert(data)
         else:
             self.data=data
     def print_tree(self):
         if(self.left):
             self.left.print_tree()
             print(self.data)
         if(self.right):
             self.right.print_tree() 
     def inorder(self,root):
         res=[]
         if root:
             res=self.inorder(root.left)
             res.append(root.data)
             res=res+self.inorder(root.right)
         return res
     def preorder(self,root):
         res=[]
         if root:
             res.append(root.data)
             res=res+self.preorder(root.left)
             
             res=res+self.inorder(root.right)
         return res
     def postorder(self,root):
         res=[]
         if root:
             res=self.inorder(root.left)
             
             res=res+self.inorder(root.right)
             res.append(root.data)
         return res
root=Node(50)
root.insert(30)
root.insert(70)
root.insert(20)
root.insert(40)
root.insert(60)
root.insert(90)
print("INORDER:",end="")
print(root.inorder(root))
print("PREORDER:",end="")
print(root.preorder(root))
print("POSTORDER:",end="")
print(root.postorder(root))


    
    
