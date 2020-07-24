#include <stdio.h>
int partition_a(int[],int,int);
void quicksort_asc(int[],int, int);
void swap(int *a,int *b)
{
    int temp=*a;
    *a=*b;
    *b=temp;
}
int partition_a(int arr[],int l,int h)
{  
     int j;
     int pivot=arr[l];
     int i;
     i=l;
     j=h+1;
    
     while(i<j)
     {
         do {
             i++;
           }
         while(arr[i]<=pivot);
            do{
              j--;
           }
          while(arr[j]>pivot);
      if(i<j)
        {
            swap(&arr[i],&arr[j]);
        } 
      }
     arr[l]=arr[j];
     arr[j]=pivot;
     return j;
   }
//apply quick sort
    void quicksort_asc(int arr[],int l,int h)
{
     int j;
    
     if(l<h)
    {
        j=partition_a(arr,l,h);
        quicksort_asc(arr,l,j-1);
        quicksort_asc(arr,j+1,h);
    }
}
int main()
{
     int a[100],s[100],f[100];
     int n;
     printf("\nenter the no of total activities:\n ");
     scanf("%d",&n);
     int i;
     printf("\n Enter the activities no:\n");
     for(i=0;i<n;i++)
     {
         scanf("%d",&a[i]);
     }
     printf("\n Enter the starting time:\n");
     for(i=0;i<n;i++)
     {
         scanf("%d",&s[i]);
     }
       
     printf("\n Enter the finishing time:\n");
     for(i=0;i<n;i++)
     {
         scanf("%d",&f[i]);
     }  
     quicksort_asc(a,0,n-1);
     quicksort_asc(s,0,n-1);
     quicksort_asc(f,0,n-1);
     /*
     for(i=0;i<n;i++)
     {
         printf("%d\n",a[i]);
     }
     for(i=0;i<n;i++)
     {
         printf("%d\n",s[i]);
     }
     for(i=0;i<n;i++)
     {
         printf("%d\n",f[i]);
     }
     */
     //int res[100];
     int j;
     int k=0;
     printf("\nthe final activities:\n");
     printf("%d\n",a[0]);
     //int c=1;
     for(j=1;j<n;j++)
     {
         if(s[j]>=f[k])
         {
             printf("%d\n",a[j]);
             k=j;
         }
     }
     

    return 0;
}
