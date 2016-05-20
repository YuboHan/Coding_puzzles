import sys

def description():
	print("Game of Threes")
	print("Rules: Given some number input x (example: " + sys.argv[0] + " 100),")
	print("the program will divide by 3 if it is able to, or add or subtract 1")
	print("before dividing by 3.")

def recursiveCall(x):
	if x == 1:
		print("Number is now 1.")
		return

	print("Current number: " + str(x))

	if x % 3 == 0:
		print("Divide by 3")
		recursiveCall(x / 3)
	elif (x + 1) % 3 == 0:
		print("Add 1, then divide 3")
		recursiveCall((x + 1) / 3)
	else:
		print("Subtract 1, then divide 3")
		recursiveCall((x - 1) / 3)

if __name__ == '__main__':
	if len(sys.argv) is not 2:
		print("Invalid arguments: will only accept a number, or --help argument.")

	elif sys.argv[1] == "--help":
		description()

	else:
		x = sys.argv[1]
		recursiveCall(int(float(x)))