# Given an amount, and possible denominations of the change, return the number of different
# ways that the change can be given such that it adds up to exactly the amount

def makeChange(amount, denominations):
	denom_coefficients = [1] + [0] * amount;

	for coin in denominations:
		for i in range(1, amount + 1):
			if coin <= i:
				denom_coefficients[i] += denom_coefficients[i - coin]

	print(denom_coefficients)
	return denom_coefficients[amount];



if __name__ == "__main__":
	amount = 30
	denominations = [1, 2, 5]

	makeChange(amount, denominations)