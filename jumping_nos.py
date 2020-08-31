n=int (input("enter the range:"))
flag=0
for i in range(n):
     if(i<=9):
         print(i)
     else:
         n=i
         if(n>0):
             rem=n%10
             n=n//10
             while(n>0):
                 rem1=n%10
                 if(abs(rem-rem1)==1):
                     flag=1
                     
                 else:
                     break
                 n=n//10
                 if(flag==1):
                     print(i)
         
