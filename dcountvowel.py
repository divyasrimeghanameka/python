s=input("enter a string:")
vowel_count=0
for i in s:
	if i in "aeiouAEIOU":
		vowel_count+=1
print("number of vowels=",vowel_count)
