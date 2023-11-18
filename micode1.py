
month = int(input("Enter a month in number:"))
year = int(input("Enter a year:"))

if(month == 1):
	print("January number of days is 31")

if(month == 3):
	print("March number of days is 31")
if(month == 5):
	print("May number of days is 31")
if(month == 7):
	print("July number of days is 31")
if(month == 8):
	print("August number of days is 31")
if(month == 10):
	print("October number of days is 31")
if(month == 12):
	print("December number of days is 31")

    
if((month == 2) and ((year % 400 == 0) or (year % 4 == 0 and year % 100 == 0))):
	print("February number of days is 29")

elif(month == 2):
	print("February number of days is 28")

if(month == 4):
	print("April number is 30")
if(month == 9):
	print("September number of days is 30")

if(month == 11):
	print("November number of days is 30")


	