def rev_list(l):
	start=0
	end=len(l)-1
	while start<end:
		l[start],l[end]=l[end],l[start]
		start=start+1
		end=end-1
	return l
list=[1,2,3,4,5]
print("acutal list: ",list)
reversed_list=rev_list(list)
print("reversed list: ",reversed_list)
		
