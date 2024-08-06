l=[]
n=int(input("enter no. of elements="))
for i in range(n):
	ele=int(input("enter the element:"))
	l.append(ele)
print(l)
l.remove(3)
print("after removing first occurance element=",l)
