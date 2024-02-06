def cube_list(digits):
	result =  []
	for number in digits:
		result += [number**3]

	return result
	
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = cube_list(number)
print(result)