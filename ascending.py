number1 = float(input("Enter an integer:"))
number2 = float(input("Enter an integer:"))
number3 = float(input("Enter an integer:"))

if number1 > number2 and number2 > number3:
	print(number3, number2, number1)
if number2 > number1 and number1 > number3:
	print(number3,  number1, number2)
if number3 > number2 and number2 > number1:
	print(number1, number2, number3)
if number1 > number3 and number3 > number2:
	print(number2, number3, number1)
if number2 > number3 and number3 > number1:
	print(number1, number3, number2)
if number3 > number1 and number1 > number2:
	print(number2, number1, number3)  