playerone = input("Enter playerone name:")

number1 = input("Enter a number from 0, 1, 2:")

playertwo = input("Enter playertwo name:")

number2 = input("Enter a number from 0, 1, 2:")

if number1 == 0 and number2 == 1:
	print(playerone +' won '+ playertwo)

if number1 == 1 and number2 == 0:
	print(playertwo +' won '+ playerone)

if number1 == 1 and number2 == 2:
	print(playertwo +' won '+ playerone) 
