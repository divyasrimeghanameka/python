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
print("pos of max ele=",l.index(a))
print("pos of min ele=",l.index(b))

