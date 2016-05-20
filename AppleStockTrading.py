import sys

def description():
	print("Apple Stocks Trading")
	print("You receive yesterday's stock price as a list, where each index is one minute after trading time.")
	print("Each index will hold the price of the stock at that time. For example, $60 3 minutes after opening")
	print("will be previous_stock_prices[3] = 60. If you are allowed one trade, find the times to buy and sell")
	print("one stock that will yield the best profit (it will be negative if price continuously drops.")

def get_max_profit(prices):
	if len(prices) < 2:
		print("stock price list not long enough. Needs at least 2 values")

	historic_min = 0
	historic_max_profit = prices[1] - prices[0]

	cur_min = 0
	cur_max_profit = historic_max_profit

	for index, price in enumerate(prices):
		if index == 0:
			continue

		cur_max_profit = max(price - prices[cur_min], cur_max_profit)

		if prices[cur_min] > price:
			if cur_max_profit > historic_max_profit:
				historic_min = cur_min
				historic_max_profit = cur_max_profit
			cur_min = index
			if index < len(prices) - 2:
				cur_max_profit = prices[index + 1] - prices[index]

	if cur_max_profit > historic_max_profit:
		historic_min = cur_min
		historic_max_profit = cur_max_profit

	# find the max
	for index, price in enumerate(prices):
		if index <= historic_min:
			continue

		if price == prices[historic_min] + historic_max_profit:
			max_index = index
			break

	print("Sell at minute " + str(historic_min))
	print("Buy at minute " + str(max_index))
	print("Profit: " + str(historic_max_profit))

if __name__ == "__main__":
	if len(sys.argv) != 1 and sys.argv[1] != "--help":
		if sys.argv[1] == "--help":
			description()
		else:
			print("Invalid argument: Use --help for description.")
		sys.exit()

	stock_prices_yesterday = [5, 6, 2, 4, 1, 8, 0, 6]
	get_max_profit(stock_prices_yesterday)