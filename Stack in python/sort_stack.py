def top(stack):
     return stack[len(stack)-1]
def sort_stack(stack):
     temp_stack=[]
     while(len(stack)!=0):
         temp=top(stack)
         stack.pop()
         #temp_stack.append(temp)
         #temp=top(stack)
     #print(temp)
         while(((len(temp_stack)!=0))and(temp<top(temp_stack))):
             stack.append(top(temp_stack))
             temp_stack.pop()
         temp_stack.append(temp)
     
     for i in range(0,len(temp_stack)):
         print(temp_stack[i],end="")
        
  
arr=[]
arr.append(1)
arr.append(3)
arr.append(4)
arr.append(2)
sort_stack(arr)
   
 
 
