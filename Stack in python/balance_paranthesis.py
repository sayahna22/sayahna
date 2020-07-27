def top(stack):
     return stack[len(stack)-1]
def isempty(stack):
     len(stack)==0
     return stack
exp=str(input("Enter the expression:"))
n=len(exp)
stack=[]
flag=0
for i in range(n):
     if(exp[i]=="("  or exp[i]=="{"or exp[i]=="["):
          stack.append(exp[i])
     elif(exp[i]==")"  or exp[i]=="}" or  exp[i]=="]"):
         if((isempty(stack))):
             flag=1
         else:
             temp=stack.pop()
             if(exp[i]==")" and ((temp=="[") or (temp=="{"))):
                 flag=1
             if(exp[i]=="}" and ((temp=="(") or (temp=="["))):
                 flag=1
             if(exp[i]=="]" and ((temp=="(") or (temp=="{"))):
                 flag=1
             else :
                 continue
     else:
         continue
if(flag==1):
     print("UnBalanced\n")
else:
    print("Balanced\n")
         
