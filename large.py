number1 = int(input("Enter first number:" ))

number2 = int(input("Enter second number:" ))

number3 = int(input("Enter third number:" ))

if number2 > number1 and number2 > number3:
	print("The largest is", number2)
if number1 > number3 and number1 > number2:
	print("The largest is", number1)
if number3 > number1 and number3 > number2:
	print("The largest is", number3)

