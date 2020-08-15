def power(a,b):
     if(b==0):
         return 1
     temp=power(a,b//2)
     if(b%2==0):
         return temp *temp
     else:
         return a*temp*temp
x=int(input())
y=int(input())
res=power(x,y)
print(res)
