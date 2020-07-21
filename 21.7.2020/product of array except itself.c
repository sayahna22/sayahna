#include <stdio.h>

int main()
{   
     printf("Enter the size of the array:\n");
     int n;
     scanf("%d",&n);
     int a[100];
     int i;
     printf("Enter the elements:\n");
     for(i=0;i<n;i++)
     {
         scanf("%d",&a[i]);
     }
     int res[100];
     int k=0;
     int l;
     int r;
     int prod=1;
     l=0;
     r=0;
     while(l<n)
     {
         r=0;
         while(r<n)
         {
             if(l==n-1)
             {
                 prod=a[r]*prod;
                 r++;
                 if(r==n-1)
                 {
                     break;
                 }
                 
             }
             if(r==l)
             {
                 r++;
                 prod=a[r]*prod;
                 r++;
             }
             else
             { 
                 prod=a[r]*prod;
                 r++;
             }
             
             //continue;
         }
         res[k++]=prod;
         prod=1;
         l++;
         
     }
     printf("\nThe Final array is:\n");
     for(i=0;i<n;i++)
     {
         printf("%d\n",res[i]);
     }
     return 0;
}
