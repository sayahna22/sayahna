def smallest_missing_no(arr:list,n:int):
     for i in range(0,n-1):
         if(arr[i]+1)==arr[i+1]:
             continue
         else:
             return (arr[i]+1)
             break;
a=[]
n=int(input("Enter the size of the array:"))
print("Enter the elements:",end="")
for i in range(n):
     ele=int(input())
     a.append(ele)
res=smallest_missing_no(a,n)
print("The smallest missing no",str(res))
