from collections import deque
queue=deque()
num=int(input("Enter the size of the queue:"))
print("The Elements are:")
for i in range(num):
     ele=int(input())
     queue.append(ele)
print("Display:")
for i in range(num):
     print(queue.popleft())
