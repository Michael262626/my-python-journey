number = int(input("Enter a digit:"))

number1 = number // 10000
remainder = number % 10000
number2 = remainder // 100
remainder1 = remainder % 100
number3 = remainder1 // 100
remainder2 = remainder1 % 100

number4 = remainder2 // 10

number5 = remainder2 % 10

print(number5)


