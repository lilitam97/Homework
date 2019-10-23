def factorial(n):
	if n > 1:
		return n * factorial(n-1)
	else:
		return 1

print(factorial(5))





class Book:
	def __init__(self, name, year, author, price):
		self.name = name
		self.year = year
		self.author = author
		self.price = price

	def get_author(self):
		return self.author

	def set_price(self, price):
		self.price = price

first_book = Book("Master and Margaret", 1967, "Michael Bulgakov", "$22")
second_book = Book("Where are you?", 2001, "Mark Levi", "$14")


print(first_book.get_author())
print(first_book.price)
first_book.set_price("$10")
print(first_book.price)






import random

def dice():
	return random.randint(1, 6), random.randint(1, 6)

print(dice())





