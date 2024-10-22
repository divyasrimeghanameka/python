import csv
data=[['sno','name','age'],[1,'divya',17],[2,'sri',12]]
with open("table.csv",'w',newline='') as file:
	s=csv.writer(file)
	s.writerows(data)
with open("table.csv",'r') as f:
	rd=csv.reader(f)
	for row in rd:
		print(row)
