def bin_search(arr:list,n:int,ele:int):
     low=0
     high=n-1
     
     while(low<high):
         mid=(low+high)//2
         if(arr[mid]==ele):
             return mid
         elif (arr[mid]>ele):
             high=mid-1
         else:
             low=mid+1
if __name__ == '__main__':
     num=int(input("Enter the size of the array:" ))
     a=[]
     print("Enter the elements:")
     for i in range(num):
         ele=int(input())
         a.append(ele)
     data=int(input ("Enter the element:"))
     res=bin_search(a,num,data)
     print(res)
     
