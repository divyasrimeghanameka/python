def multiple_returns(a,b):
	return a+b,a-b
sum,sub=multiple_returns(12,2)
print("sum: ",sum)
print("sub: ",sub)
