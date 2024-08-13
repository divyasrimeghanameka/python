l=[]
n=int(input("enter noi. of elements="))
for i in range(n):
	ele=int(input("enter an element="))
	l.append(ele)
print(l)
a=max(l)
b=min(l)
print("maximum number=",a)
print("minimum number=",b)
