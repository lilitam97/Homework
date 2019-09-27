import random

number_of_games= int(input("How many games would you like to play?: "))

for i in range(0, number_of_games):
	hidden_number = random. randint(1,100)

	user_guess = 0 

	while not user_guess == hidden_number:
		user_guess = int(input("Guess a number: "))

		if user_guess > hidden_number:
			print("Too high!")

		elif user_guess < hidden_number:
			print("Too low!")

		else:
			print("That's right!")