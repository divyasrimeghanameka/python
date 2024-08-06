l=[]
n=int(input("enter no.of elments="))
for i in range(n):
	ele=int(input("enter element="))
	l.append(ele)
print(l)
l[-1], l[0]=l[0], l[-1]
print("list after interchanging:",l)
