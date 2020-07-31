#include <stdio.h>
void swap(int *a,int *b)
{
     int temp= *a;
     *a=*b;
     *b=temp;
}
void heapify(int a[100],int n,int i)
{
     int largest=i;
     int left=2*i+1;
     int right=2*i+2;
     if(left<n && a[largest]<a[left])
     {
         largest=left;
     }
     if(right<n && a[largest]<a[right])
     {
         largest=right;
     }
     if(largest!=i)
     {
         swap(&a[i],&a[largest]);
         heapify(a,n,largest);
     }
}
void heap_sort(int a[100],int n){
     int i;
     for(i=n/2-1;i>=0;i--)
     {
         heapify(a,n,i);
     }
     for(i=n-1;i>0;i--)
     {
         swap(&a[0],&a[i]);
         heapify(a,i,0);
     }
}
int main()
{
     int n;
     printf("Enter the size of the array:\n");
     {
         scanf("%d",&n);
     }
     int a[100],i;
     printf("Enter the elements:\n");
     for(i=0;i<n;i++)
     {
         scanf("%d",&a[i]);
     }
     heap_sort(a,n);printf("Sorted Array");
     for(i=0;i<n;i++)
     {
         printf("%d ",a[i]);
     }
    return 0;
}
