fruits = {"apples": 5, "oranges": 14, "pineapple": 1, "bananaas": 4, "pomegranate": 7}

for key in fruits.keys():
	if fruits[key] > 5:
		print(key)






grades = {"Gor": 26, "David": 26, "Rafael": 28, "Khachatur": 23, "Marat": 24, "Marianna": 25}

for (name, estimates) in grades.items():
	print(name, "gets", estimates, "points.")

grades["Rafael"] = 100
print(grades)






classes = {"Math": ["Davit", "Lucy", "Dana"],
			"Physics": ["Addison", "Ava"],
			"Chemistry": ["Sara", "Arthur"]}

print("Students in math class", classes["Math"])
classes["Math"].append("Lilit")
print("Students in math class", classes["Math"])






mydreams = {"car": ["BMW M3 E46", "Audi R7"],
			"travelto": ["Chinese Wall", "Amsterdam", "Antarctica"],
			"learn": ["python", "mathematics", "biology"]}


mydreams["car"] = "Mercedes Benz G500"
mydreams["learn"].append("drifting, donuts, burnouts")


print("Here are several life goals for the next 2 years", mydreams["car"], mydreams["travelto"], mydreams["learn"])







sample_text = "Having a conversation with your computer might sound like the script of a science fiction movie. After all, the members of the Enterprise on Star Trek regularly talked with their computer. In fact, the computer often talked back. However, with the rise of Apple’s Siri and other interactive software, perhaps you really don’t find a conversation so unbelievable."

words_dict = {}

sample_text = sample_text.lower()
sample_text = sample_text.replace(',', "")
sample_text = sample_text.replace('.', "")
sample_text = sample_text.split(" ")

for word in sample_text:
	if word in words_dict.keys():
		words_dict[word] += 1
	else:
		words_dict[word] = 1

for (word, amount) in words_dict.items():
	if amount > 2:
		print(word, ":", amount)




