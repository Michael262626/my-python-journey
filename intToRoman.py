def intToRoman(number):
       m = ["", "M", "MM", "MMM"]
       c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
       x = ["", "X", "XX", "XXX", "Xl", "L", "LX", "LXX", "LXXX", "XC"]
       i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

       thousands = m[number // 1000]
       hundreds = c[(number % 1000) // 100]
       tens = x[(number % 100) // 10]
       ones = i[number % 10]

       ans = (thousands + hundreds + tens + ones)

       return ans
number = 12
print(intToRoman(number))