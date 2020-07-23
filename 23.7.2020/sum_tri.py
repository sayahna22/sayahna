def sum_tri(arr:list,n:int):
     #b=range(n-1)
     if (n < 1): 
       return
            
     b=[0]*(n-1)#initialize a list b
     for i in range(0,n-1):
         s=arr[i]+arr[i+1]
         b[i]=s
     sum_tri(b,n-1)
     print(arr)
if __name__ == '__main__':
     num=int(input("Enter the size:"))
     a=[]
     for i in range(num):
         ele=int(input())
         a.append(ele)
     sum_tri(a,num)
     

