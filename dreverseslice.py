l=[]
n=int(input("enter no of elements:"))
for i in range(n):
	ele=int(input("enter an element="))
	l.append(ele)
print(l)
print("reversed list=",l[::-1])
