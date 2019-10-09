def tuple1():
	user_name = input("Enter your name: ")
	user_surname = input("Enter your surname: ")
	return user_name, user_surname

user_info = tuple1()

print("Your name is " + user_info[0])
print("your surname is " + user_info[1])






nested_tuple = ((1,2), (3, 4), (5, 6))

print(nested_tuple[0])
print(nested_tuple[0] [0])