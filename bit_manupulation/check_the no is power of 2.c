#include <stdio.h>
int main()
{
     printf("Enter The number:");
     int num;
     scanf("%d",&num);
     if((num & (num-1))==0)
     {
         printf("It is the power of 2 no");
     }
     else{
         printf("It is not the no");
     }
     return 0;
}
