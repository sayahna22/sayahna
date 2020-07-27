name=str(input("Enter the string:"))
stack=[]
for i in range(len(name)):
     stack.append(name[i])
print("The reversed string:")
for i in range(len(stack)):
     print(stack.pop(),end="")
     
