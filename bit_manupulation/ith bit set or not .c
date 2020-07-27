#include <stdio.h>

int main()
{
     int num;
     printf("Enter the no:");
     scanf("%d",&num);
     int k;
     printf("Enter the bit");
     scanf("%d",&k);
     if((num& (1<<k))!=0){
         printf("present");
     }
     else{
         printf("Not present");
     }

    return 0;
}
