def count_1_bin(num:int):
     a=[0]*num
     k=0
     while(num>0):
         a[k]=num%2
         num=num//2
         k=k+1
     a.reverse()
     #print(a)
     c=0
     for i in range(len(a)):
         if(a[i]==1):
             c=c+1
     return c
num=int(input("Enter the element:"))
res=count_1_bin(num)
print("The count is:",str(res))
