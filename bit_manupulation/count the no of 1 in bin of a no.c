#include <stdio.h>

int main()
{
     int num;
     printf("Enter the number");
     scanf("%d",&num);
     int count=0;
     while(num>0)
     {
         num=num &(num-1);
         count++;
     }
     printf("The count of 1 is:%d",count);
    return 0;
}
