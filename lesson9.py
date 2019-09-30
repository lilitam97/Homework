def even_or_odd(number):
	if number % 2 == 0:
		return "even"
	return "odd"
ask_number = input("enter some number: ")

print(even_or_odd(int(float(ask_number))))