# num1 = int(input("first number: "))
# num2 = int(input("second number: "))
# num3 = int(input("third number: "))

# def max_number (num1, num2, num3):


# 	temp = num1
# 	if num2 > temp:
# 		temp = num2

# 	if num3 > temp:
# 		temp = num3

# 	return temp


# print(max_number(num1, num2, num3))






given_number = int(input("Insert a number: "))

a = 3
b = 5

def fizz_buzz (a, b):
	if  given_number % a == 0 and given_number % b == 0:
		return str("FizzBuzz")
	
	elif given_number % a == 0:
		return str("Fizz")
	elif given_number % b == 0:
		return str("Buzz")
	if given_number % a != 0 or given_number % b != 0:
		return str("This number is not divisible by 3 or 5.")
	

print(fizz_buzz(a, b))