price = int(input("Enter the price :"))

if price < 1000000:
	result = (10 / 100) * price
	print(result)

if price == 1000000 and price < 3000000:
	result = (15 / 100) * price
	print(result)

if price == 3000000 and price < 5000000:
	result = (20 / 100) * price
	print(result)

if price >= 5000000:
	result = (25 / 100) * price
	print(result)