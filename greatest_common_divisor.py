def greatest_common_divisor(num1, num2):
	divisor = num1/num2
	result = num1%num2
	final_result = result + divisor

	return final_result
number1 = int(input("Enter 2 digit number:"))
number2 = int(input())
result = greatest_common_divisor(number1, number2)
print(result)