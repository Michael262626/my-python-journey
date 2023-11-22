number = int(input("Enter an integer:"))

number1 = number // 10000
remainder = number % 10000
number2 = remainder // 1000
remainder1 = remainder % 1000

number3 = remainder1 // 100
remainder2 = remainder1 % 100

number4 = remainder2 // 10

number5 = remainder2 % 10
print(number1,"\t", number2,"\t", number3, "\t", number4,"\t", number5)



