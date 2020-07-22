#include <stdio.h>
int partition_a(float[],int,int);
void quicksort_asc(float[],int, int);
void swap(float *a,float *b)
{
    float temp=*a;
    *a=*b;
    *b=temp;
}
int partition_a(float arr[],int l,int h)
{  
     int j;
     float pivot=arr[l];
     int i;
     i=l;
     j=h+1;
    
     while(i<j)
     {
         do {
             i++;
           }
         while(arr[i]<=pivot);
            do{
              j--;
           }
          while(arr[j]>pivot);
      if(i<j)
        {
            swap(&arr[i],&arr[j]);
        } 
      }
     arr[l]=arr[j];
     arr[j]=pivot;
     return j;
   }
//apply quick sort
    void quicksort_asc(float arr[],int l,int h)
{
     int j;
    
     if(l<h)
    {
        j=partition_a(arr,l,h);
        quicksort_asc(arr,l,j-1);
        quicksort_asc(arr,j+1,h);
    }
}
int main()
{
     printf("\nEnter the no of elememts:\n ");
     int n;
     scanf("%d",&n);
     printf("\nEnter the Weight  array:\n");
     float w[100];
     int i;
     for(i=0;i<n;i++)
     {
         scanf("%f",&w[i]);
     }
     printf("\nEnter the profit array:\n");
     float p[100];
     for(i=0;i<n;i++)
     {
         scanf("%f",&p[i]);
     }
     printf("\nEnter the bag capacity:\n");
     int cap;
     scanf("%d",&cap);
     //float rat[100];
     /*
     for(i=0;i<n;i++)
     {
         rat[i]=p[i]/w[i];
     }*/
     quicksort_asc(p,0,n-1);
     quicksort_asc(w,0,n-1);
     //quicksort_asc(rat,0,n-1);
     /*
     for(i=0;i<n;i++)
     {
         printf("%.2f\t",w[i]);
     }
     printf("\n");
     for(i=0;i<n;i++)
     {
         printf("%.2f\t",p[i]);
     }
     printf("\n");
     for(i=0;i<n;i++)
     {
         printf("%.2f\t",rat[i]);
     }
     //quicksort_asc((rat,0,n-1);
     */
     float x[100];
     
     for(i=0;i<n;i++)
     {
         x[i]=0.0;
     }
     int j;
     //int max=0;
     //int k;
     //float rat_x;
     float tot_prof=0;
     float m=(float)cap;
     for(i=0;i<n;i++)
     {
         if(w[i]>m)
         {
             break;
         }
         else
         {
             x[i]=1.0;
             tot_prof=tot_prof+p[i];
             m=m-w[i];
             
         }
     }
     if(i<n)
     {
         x[i]=m/w[i];
     }
     tot_prof=tot_prof+(tot_prof *x[i]);
        
     printf("\nThe fraction array is:\n");
     for(i=0;i<n;i++)
     {
         printf("%.2f\n",x[i]);
     }
     /*
     for(i=0;i<n;i++)
     {
         tot_prof=tot_prof+(x[i]*p[i]);
     }
     */
     printf("\n The profit will be:%.2f",tot_prof);
return 0;
}

   

