l=[]
n=int(input("enter no. of elements:"))
for i in range(n):
	ele=int(input("enter the element="))
	l.append(ele)
print(l)
print("sum of elemnets in the list=",sum(l))
print("average of elemnts in the list=",sum(l)//len(l))
