amount = float(input("Enter your investment amount:"))
years = int(input("Enter the number of years:"))

amount_of_deposit = amount * (1 + 7 / 100) * years * years

print("The amount of deposit at the end of the year is", amount_of_deposit)