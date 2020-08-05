#list defining
lis=[1,2,3,4,5,6]
print(lis)
lis1=[7,8,9,10]
print(lis1)
#list in list
main=[lis,lis1]
print(main)
#list is Mutable
#insert value at a pos
lis.insert(4,12)
print(lis)
#remove value
lis.remove(1)
print(lis)
#pop frespect to a index
lis.pop(4)
print(lis)
#pop from the last
lis.pop()
print(lis)
#delete multiple values
del lis[2:]
print(lis)
#adding Multiple values
lis.extend([9,6,10,55])
print(lis)
#find min value
print(min(lis))
#find max value
print(max(lis))
#sort the list
lis.sort()
print(lis)
