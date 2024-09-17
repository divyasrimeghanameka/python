def add_key_value(dictionary,key,value):
	dictionary[key]=value
	return dictionary
my_dict={'a':10,'b':20,'c':30,'d':40}
updated_dict=add_key_value(my_dict,'e',50)
print("dictionary after add a key-value pair: ",updated_dict)
