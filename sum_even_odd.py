def even_sum(numbers):
	even_sum = 0
	for number in range(2, numbers, 2):
		if number % 2 == 0:
			even_sum += number
	return even_sum

def odd_sum(numbers):
	odd_sum = 0
	for number in range(1, numbers, 2):
		if number % 2 != 0:
			odd_sum += number
	return odd_sum

numbers = int(input('Enter a number: '))
print(even_sum(numbers))
print(odd_sum(numbers))