
n=int(input("Enter the number:"))
arr=[0]*n*2
print("The series will be:")
s=0
for i in range(n*2):
     if(i%2==0):
         arr[i]=i
     else:
         arr[i]=s+arr[i]
         s+=1
print(arr)
