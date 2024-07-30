a=int(input("enter an year="))
if a%4==0 and a%100!=0:
  print(a,"is a leap year")
elif a%400==0:
  print(a,"is leap year")
else:
  print(a,"is not leap year")
