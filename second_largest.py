l=[123,456,821,9421,5463,1002,2005,245]
def second_largest(l):
	l.sort()
	return l[-2]
print("the second largest number is ",second_largest(l))
