l=[]
n=int(input("enter no of elements="))
for i in range(n):
	ele=int(input("enter the value="))
	l.append(ele)
print(l)
l.reverse()
print("reversed list=",l)
