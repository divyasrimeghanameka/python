n=int(input("enter no of rows:"))
l=65
for i in range(1,n+1):
	for j in range(1,i+1):
		print(chr(l),end=" ")
		l+=1
	print(" ")
	 
