#include <stdio.h>

int main()
{
     int n;
     printf("Enter the size of the array:\n");
     scanf("%d",&n);
     int a[100];
     int i;
     printf("Enter the Elements:\n");
     for(i=0;i<n;i++)
     {
         scanf("%d",&a[i]);
     }
     int temp,j;
     for (i=1;i<n;i++)
     {
         temp=a[i];
         j=i-1;
         while(j>=0 && a[j]>temp){
             a[j+1]=a[j];
             a[j]=temp;
             j--;
         }
         a[j+1]=temp;
     }
     printf("The sorted array is:\n");
     for(i=0;i<n;i++)
     {
         printf("%d ",a[i]);
     }
    return 0;
}
