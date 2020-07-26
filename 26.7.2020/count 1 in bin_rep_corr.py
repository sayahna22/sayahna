num=int(input("Enter The Number:"))
c=0
while(num>0):
     num=(num  & num-1)
     c=c+1
print("The no of one",c)
