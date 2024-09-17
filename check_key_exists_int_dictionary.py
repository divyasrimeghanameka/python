def check_key_exists(dict,key):
	if key in dict:
		print("key ",key," exists in the dictionary")
	else:
		print("key ",key," not exist in the dictionary")
my_dict={"name":"divya","age":18,"perc":97,"rollno":234}
check_key_exists(my_dict,"age")
check_key_exists(my_dict,"email")
