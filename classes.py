class PySolution:
	def roman_to_int(self, string):
		rom_val = {"I": 1, "V": 5, "X": 10, "L": 50,
					"C": 100, "D": 500, "M": 1000}
		int_val = 0

		for i in range(len(string)):
			if i > 0 and rom_val[string[i]] > rom_val[string[i-1]]:
				int_val += rom_val[string[i]] - 2 * rom_val[string[i-1]]
			else:
				int_val += rom_val[string[i]]
		return int_val

print(PySolution().roman_to_int("IX"))
print(PySolution().roman_to_int("MMMCMLXXXVI"))
print(PySolution().roman_to_int("MDCL"))
print(PySolution().roman_to_int("MMMM"))





class Rectangle:
	def __init__(self, l, w):
		self.length = l
		self.width = w

	def rectangle_area(self):
		return self.length * self.width

	def rectangle_perimeter(self):
		return (self.length + self.width) * 2

rectangle_l = int(input("Input rectangle length: "))
rectangle_w = int(input("Input rectangle width: "))

my_rectangle = Rectangle(rectangle_l, rectangle_w)

print(my_rectangle.rectangle_area())
print(my_rectangle.rectangle_perimeter())





class Card:
	def __init__(self, suit, val):
		self.suit = suit
		self.value = val

	def show(self):
		print(f"{self.value} of {self.suit}")

card = Card("Card", 6)
card.show()

class Deck:
	def __init__(self):
		self.cards = []
		self.build()
	def build(self):
		for s in ["spades", "hearts", "diamonds", "clubs"]:
			for v in range(2, 14):
				self.cards.append(Card(s,v))
	def show(self):
		for c in self.cards:
			c.show()

deck = Deck()
deck.show()





class Circle:
	def __init__(self, r):
		self.radius = r

	def area(self):
		return self.radius **2 * 3.14

	def perimeter(self):
		return 2 * self.radius * 3.14

new_circle = Circle(8)

print(new_circle.area())
print(new_circle.perimeter())





import math

print(len(str(math.pi)))
class Circle:
	def __init__(self, r):
		self.radius = r

	def area(self):
		return self.radius **2 * math.pi

	def perimeter(self):
		return 2 * self.radius * math.pi

new_circle = Circle(8)

print(new_circle.area())
print(new_circle.perimeter())