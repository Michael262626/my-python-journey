def int_to_roman(val, syb):
	val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
	syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

	roman_num = ""
	count = 0
	for count in range(num // val[count]):
		roman_num += syb[count]
		num -= val[count]
			
		count += 1
		
		return roman_num 
	
user_input = input('Enter number: ')
	
string_array = int_to_roman(user_input, "")
print(f"{user_input} is Roman numeral is: {string_array}")