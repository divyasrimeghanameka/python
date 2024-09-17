def cal(a,b):
	add=a+b
	sub=a-b
	mul=a*b
	div=a/b
	rem=a%b
	return add,sub,mul,div,rem
add_result,sub_result,mul_result,div_result,rem_result=cal(12,2)
print("sum: ",add_result)
print("sub: ",sub_result)
print("mul: ",mul_result)
print("div: ",div_result)
print("rem: ",rem_result)
	
