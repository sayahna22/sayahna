#include <stdio.h>

int main()
{
     printf("Enter the  size of the array:\n");
     int n;
     scanf("%d",&n);
     int a[100];
     printf("Enter the elements:\n");
     int i;
     for(i=0;i<n;i++)
     {
         scanf("%d",&a[i]);
     }
     printf("\nEnter the sum:");
     int sum;
     scanf("%d",&sum);
     int j;
     for(i=0;i<n;i++)
     {
         for(j=i+1;j<n;j++)
         {
             if(a[i]+a[j]==sum)
             {
                 printf("\nThe elements of these %d %d indexes %d %d",i,j,a[i],a[j]);
             }
         }
     }
     return 0;
}
