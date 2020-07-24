def fact(n:int):
     if(n==1):
         return n
     else:
         return (n*fact(n-1))
num=int(input("Enter the num:"))
res=fact(num)
print(res)
   
