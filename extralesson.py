input_string = input("Enter some string: ").split()
new_list = []

for i in range(len(input_string)):
	new_list.append(input_string[i].upper())

input_string = ""
print(new_list)
print(input_string.join(new_list))





def calculate_members(string):
	digits = 0
	letters = 0
	for char in string:
		if char.isalpha():
			letters += 1
		if char.isdigit():
			digits += 1
	return digits, letters

user_string = input("Enter some string: ")

digits, letters = calculate_members(user_string)

print("Num of digits", digits, "and number of letters", letters)




import random
import string

def randomString(stringlength = 10):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(stringlength))

rand_string = randomString(3)
print(rand_string)

def guess_letters():
	guess = False
	len_of_random_string = len(rand_string)
	guessed_letters_amount = 0


	while guess == False:
		if guessed_letters_amount != len_of_random_string:
			letter = input("enter a letter")
			while not (letter.isalpha() and len(letter) == 1):
				print("you have entered not valid characters")
				letter = input("enter a letter")
			for i in rand_string:
				if letter == i:
					guessed_letters_amount += 1
					print("letter was found")
		else:
			guess = True
			print("You found a word", rand_string)
guess_letters()