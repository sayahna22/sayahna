def heapify(a,n,i):
     largest=i
     left=2*i+1
     right=2*i+2
     if(left<n and a[largest]<a[left]):
         largest=left
     if(right<n and a[largest]<a[right]):
         largest=right
     if(largest!=i):
         a[i],a[largest]=a[largest],a[i]
         heapify(a,n,largest)
def heap_sort(arr):
     n=len(a)
     #build max-heap
     for i in range(n//2,-1,-1):
         heapify(a,n,i)
     #swap with the root 
     for i in range(n-1,0,-1):
         a[i],a[0]=a[0],a[i]
         heapify(a,i,0)
         
a=[]
n=int(input("Enter the size of the array:"))
print("\nEnter the elements:")
for i in range(0,n):
     ele=int(input())
     a.append(ele)
heap_sort(a)
print("\nSorted array is:\n")
for i in range(0,n):
     print("%d" %a[i],end=" ")
