class Person:
	def __init__(self, first_name, last_name, eye_color):
		self.first_name = first_name
		self.last_name = last_name
		self.eye_color = eye_color


my_person = Person("Lilit", "Amirkhanyan", "greenish brown")
my_person2 = Person("Khachatur", "Khachatryan", "hazel")

print(my_person.first_name)
print(my_person.last_name)
print(my_person.eye_color)


print(my_person2.first_name)
print(my_person2.last_name)
print(my_person2.eye_color)






class BankAccount:
	def __init__(self, name, balance=0.0):
		self.log("Account created!")
		self.name = name
		self.balance = balance

	def getBalance(self):
		self.log("Balance checked at " + str(self.balance))
		return self.balance

	def deposit(self, amount):
		self.balance += amount
		self.log("+" + str(amount) + ": " + str(self.balance))

	def withdraw(self, amount):
		self.balance -= amount
		self.log("-" + str(amount) + ": " + str(self.balance))

	def log(self, message):
		print(message)


my_bank_account = BankAccount("Lilit Amirkhanyan")
my_bank_account.deposit(20.0)
my_bank_account.getBalance()
my_bank_account.withdraw(10.0)
my_bank_account.getBalance()






class Person:
	def __init__(self, name, eyecolor, age):
		self.name = name
		self.eyecolor = eyecolor
		self.age = age

my_person1 = Person("Lilit Amirkhanyan", "brown", 22)

my_person2 = Person(my_person1.name, my_person1.eyecolor, my_person1.age)

print(my_person1.name)
print(my_person2.name)

my_person1.name = "aaa"

print(my_person1.name)
print(my_person2.name)





class Name:
 	def __init__(self, first_name, last_name):
 		self.first_name = first_name
 		self.last_name = last_name

class Person:
 	def __init__(self, name, eyecolor, age):
 		self.name = name
 		self.eyecolor = eyecolor
 		self.age = age

my_name = Name("lilit", "amirkhanyan")
my_person = Person(my_name, "brown", 22)

# print(my_person.name)
# print(my_person.name.first_name)
# print(my_person.name.last_name)
# print(my_person.age)

def capitalize_name(name):
	name.first_name = name.first_name.upper()
	name.last_name = name.last_name.upper()

capitalize_name(my_name)

print(my_person.name.first_name, my_person.name.last_name)