def count_rotations(arr:list,n:int):
     minim=a[0]
     c=1
     for i in range(1,n-1):
         if(minim<arr[i]):
             minim=arr[i]
             c=c+1
     return c
a=[]
n=int(input("Enter the size of the array:"))
print("Enter the elements:",end="")
for i in range(0,n):
     ele=int(input())
     a.append(ele)
res=count_rotations(a,n)
print("The count is:",str(res))
