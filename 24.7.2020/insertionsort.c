#include <stdio.h>

int main()
{
     printf("Enter the size of the array is:");
     int n;
     scanf("%d",&n);
     int arr[100];
     int i;
     printf("\nThe elements:\n");
     for(i=0;i<n;i++)
     {
         scanf("%d",&arr[i]);
     }
     int temp;
     int j;
     for(i=1;i<n;i++)
     {
         temp=arr[i];
         j=i-1;
         while( arr[j]>temp && j>=0)
         {
             arr[j+1]=arr[j];
             j--;
         }
         arr[j+1]=temp;
     }
     printf("\nSorted array is:\n");
     for(i=0;i<n;i++)
     {
         printf("%d\n",arr[i]);
     }
    return 0;
}
