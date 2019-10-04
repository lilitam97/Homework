ameria = "0001"
converse = "0002"
ineco = "0003"
evoca = "0004"
american_express = "0005"

balance = 500

def check_balance (purchase_price):
	if purchase_price > balance:
		return "You don't have enough balance"
	else: 
		return "Your balance after purchase is" + str( balance - purchase_price)

def validate_credit_card(card_number):
	if len(card_number) == 16 and card_number[0:4] != american_express:
		return True
	elif len(card_number) == 15 and card_number [0:4] == american_express:
		return True
	else:
		return False

def check_card_bank(card_number):
	if card_number[0:4] == ameria:
		return "Ameria bank"
	elif card_number[0:4] == converse:
		return "Converse Bank"
	elif card_number[0:4] == ineco:
		return "ineco Bank"
	elif card_number[0:4] == evoca:
		return "Evoca Bank"
	else:
		return "American Express Bank"

card = input("Enter your card number: ")

if validate_credit_card(card):
	print("Your credit card belongs to " + check_card_bank(card))
	purchase = input("Enter your purchase price: ")
	while not check_balance(int(purchase)):
		print(check_balance(int(purchase)))
else:
	print("You've entered wrong credentials.")

