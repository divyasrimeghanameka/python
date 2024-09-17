def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b,a%b)
a=int(input("enter numbr 1:"))
b=int(input("enter numbr 2:"))
print("gcd of ",a," and ",b," is ",gcd(a,b))
