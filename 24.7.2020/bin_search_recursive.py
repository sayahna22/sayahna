def bin_search(arr:list,low:int,high:int,ele:int):
     
     if(low<=high):
         mid=(low+high)//2
         if(arr[mid]==ele):
            print(mid)
         elif(arr[mid]>ele):
              bin_search(arr,low,mid-1,ele)
         elif(arr[mid]<ele):
             bin_search(arr,mid+1,high,ele)
         else:
             return -1

if __name__ == '__main__':
     num=int(input("Enter the size of the array:" ))
     a=[]
     print("Enter the elements:")
     for i in range(num):
         ele=int(input())
         a.append(ele)
     data=int(input ("Enter the element:"))
     bin_search(a,0,num,data)
     """
     if (res!=-1):
       print("The value found",str(res))
     else:
       print("Not found")
       """
