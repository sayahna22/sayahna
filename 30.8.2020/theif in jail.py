n=int(input("Enter the no of walls:"))
h=[]
jump=0
for i in range(n):
     ele=int(input())
     h.append(ele)
x=int(input("Rise"))
y=int(input("Fall"))
for i in range(n):
     hight=h[i]
     if(hight<x):
         
         jump+=1
     else:
         while(hight>x):
             jump+=1
             hight=hight-(x-y)
         jump+=1
print(jump)
