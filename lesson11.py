apranqi_gumar = 500

grpani_gumar = int(input("inchqana motid gumary? "))

try:
	if apranqi_gumar > grpani_gumar:
		print("Qo gumary chi heriqum vor arevtur anes.")
except:
		print("hangist gni et apranqy!")




num1 = 12
num2 = int(input("tiv asa bajanem: "))


try:
	num1 / num2
	print(num1 / num2)

except:
	print("chi bajanvum. krkin pordzir!")




my_string = "this string is not a number"

try:
	print("converting my string to int...")
	print("string #" + 1 +": " + my_string)
	my_int = int(my_string)
	print(my_int)

except ValueError:
	print("cant convert: my_string to a number")

except TypeError:
	print("cant concatinate number with string")

except:
	print("Unknown error")

print("Done!")



try:
	input_file = open("NumberFile.txt", mode = "r")

	try:
		for line in input_file:
			print(int(line))

	except ValueError:
		print("A value error occurred")

	else:
		print("No errors occurred")

	finally:
		input_file.close()
except IOError:
	print("An error occurred reading the file!")




while True:
	try:
		x = int(input("Enter a number: "))
		y = int(input("Enter another number: "))
		print(x, "/" , y, "=" , x/y)
		break
	except ZeroDivisionError:
		print("Can't divide by zero!")
	except ValueError:
		print("That doesn't look like a number!")
	except:
		print("Somehting unexpected happened!")