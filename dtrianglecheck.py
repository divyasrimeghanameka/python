a=int(input("enter the first side="))
b=int(input("enter the second side="))
c=int(input("enter the thrid side="))
if a+b>c and a+c>b and b+c>a: 
   print("triangle is valid with sides",a,b,c)
else:
   print("tringle is not valid with sides",a,b,c)
