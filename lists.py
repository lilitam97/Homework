my_list = [1,0,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

my_list.remove(23)
print(my_list, ": After removing 23")

my_list.sort()
print(my_list, ": After sorting")

my_list.reverse()
print(my_list, ": After reversing")

my_list.pop()
print(my_list, ": After poping")

del my_list [-5:]
print(my_list, ": After deleting the last five items")





my_list = [1,2,3,4]

my_list.append(5)
print(my_list, ": After appending five")

new_list = [6,7,8]
my_list.extend(new_list)
print(my_list, ":After extending")

my_list.insert(0,0)
print(my_list, ":After inserting zero")




def average(in_list):
	sum = 0
	for number in in_list:
		sum += number
	return sum/len(in_list)

my_list1 = [1,2,3,4,5,6,7]
my_list2 = [91, 92, 93, 94, 95, 96, 97]

print("The average of my_list1 is: ", average(my_list1))
print("The average of my_list2 is: ", average(my_list2))





def two_D_average(in_2d_list):
	result = []

	for num_list in in_2d_list:
		sum = 0
		for number in num_list:
			sum += number

		result. append(sum/len(num_list))

	return result

my_2d_list = [[61, 32, 12, 123], [123, 131, 131, 123], [4, 1, 2]]

print("averages: ", two_D_average(my_2d_list))