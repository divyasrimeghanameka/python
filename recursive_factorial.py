def fact(n):
	if n==0:
		return 1
	else:
		return n*fact(n-1)
n=int(input("enter a number:"))
if n<=0:
	print("please enter a positive number")
else:
	print("factorial of ",n," is ",fact(n))
