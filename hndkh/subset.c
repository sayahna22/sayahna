#include <stdio.h>

int main()
{
     printf("\nenter the size:\n");
     int n;
     scanf("%d",&n);
     printf("\nEnter the elements:\n");
     int a[100];
     int i,k;
     for(i=0;i<n;i++)
     {
         scanf("%d",&a[i]);
     }
     int j;//=i+1;
     for(i=0;i<n;i++)
     {
         for(j=i+1;j<n;j++)
         {
             if(a[i]==a[j])
             {
                 for(k=j;k<n;k++)
                 {
                     a[k]=a[k+1];
                 }
                 j--;
                 n--;
                 
             }
             
         }
     }
     printf("\nThe final array:\n");
     for(i=0;i<n;i++)
     {
         printf("%d\n",a[i]);
     }
     
     

    return 0;
}

