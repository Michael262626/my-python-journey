def check_duplicate(fruit):
	for count in range(len(fruit)):
		for index in range(count+1, len(fruit)):
			if(fruit[count] == fruit[index]):
				return f"{fruit[count]} has a duplicate"
		return f"it has no duplicate found"
fruit = ['apple', 'orange', 'banana', 'apple']
print(check_duplicate(fruit))