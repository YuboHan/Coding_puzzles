import sys

def description():
	print("Product of all other numbers aside from current")
	print("Given an array of size n, return an array of same")
	print("size, where each index is the product of all elements")
	print("inside the given array, except for the number at the")
	print("index")

def get_products(int_array):
	products = []
	products.append(1)

	i = len(int_array) - 2
	while i >= 0:
		products.insert(0, products[0] * int_array[i + 1])
		i -= 1

	cur_product = 1

	i = 1
	while i < len(int_array):
		cur_product *= int_array[i - 1]
		products[i] *= cur_product
		i += 1

	for product in products:
		print(str(product))


if __name__ == "__main__":
	if len(sys.argv) == 2 and sys.argv[1] == "--help":
		description()

	else:
		int_array = [1, 2, 3, 5]
		get_products(int_array)