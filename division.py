any_number = int(input("Insert a number you want to devide by 5 or 11: "))

x = 5
y = 11
n = "any number"

if (any_number%x) == 0 and (any_number%y) == 0:
	print("The number is divisible by 5 an 11.")
else:
	print("The number is not divisible by 5 and 11.")