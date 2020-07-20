#include <stdio.h>
#include<string.h>
void swap(char *a, char *b)
{
     char temp=*a;
     *a=*b;
     *b=temp;
}
int main()
{
     printf("Enter a String:\n");
     char ch[100];
     scanf("%s",ch);
     int n=strlen(ch);
     int i=0;
     int j=n-1;
     while(i<j)
     {
         swap(&ch[i],&ch[j]);
         i++;
         j--;
     }
     printf("The Reversed string is:\n%s",ch);
     return 0;
}
