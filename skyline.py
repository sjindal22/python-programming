def myfunc(string_input):
	x = 1
	mylist = [] 
	formatted_string = ''
	
	for letter in string_input:
		mylist.append(x)
		x += 1

	for letter, index in zip(string_input, mylist):
		print(index, letter)
		if index%2 != 0 and letter.isupper():
			letter =  letter.lower()
		elif index%2 == 0 and letter.islower():
			letter =  letter.upper()
		formatted_string += letter
	
	print(formatted_string)

myfunc('ShIviKA')
