arr=[]
num=(int(input("Ente the size of the stack")))
for i in range(num):
     ele=int(input())
     arr.append(ele)
while(len(arr)!=0):
     print(arr.pop())
