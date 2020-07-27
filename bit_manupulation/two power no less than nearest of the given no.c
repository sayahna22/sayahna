#include <stdio.h>

int main()
{
     int num;
     printf("Enter the number");
     scanf("%d",&num);
     num=num|num>>1;
     num=num|num>>2;
     num=num|num>>4;
     num=num|num>>8;
     printf("%d",((num+1)>>1));
    return 0;
}
