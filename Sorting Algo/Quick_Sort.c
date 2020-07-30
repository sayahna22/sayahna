#include <stdio.h>
void swap(int *a,int *b)
{
     int temp=*a;
     *a=*b;
     *b=temp;
}
int partition(int a[100],int l,int h)
{
     int i,j;
     i=l;
     j=h+1;
     int pivot=a[i];
     while(i<j)
     {
         do
         {
             i++;
         }while(a[i]<=pivot);
         do
         {
             j--;
         }while(a[j]>pivot);
     if(i<j)
     {
         swap(&a[i],&a[j]);
     }
     }
     a[l]=a[j];
     a[j]=pivot;
     
     return j;
}
void quick_sort(int a[100],int l,int h){
     int j;
     if(l<h){
         j=partition(a,l,h);
         quick_sort(a,l,j-1);
         quick_sort(a,j+1,h);
     }
}
int main()
{
     int n;
     printf("Enter the size of the array is:\n");
     scanf("%d",&n);
     int a[100],i;
     printf("Enter the elements:\n");
     for(i=0;i<n;i++)
     {
         scanf("%d",&a[i]);
     }
     quick_sort(a,0,n-1);
     printf("Sorted Array\n");
     for(i=0;i<n;i++)
     {
         printf("%d ",a[i]);
     }

    return 0;
}
