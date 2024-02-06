def sport_recommender(nunber):
		
	if number <= 30 and number <= 20:
		return"It's lovely weather for sports today"
	elif number <= 10 and number <= 40:
		return"It's reasonable weather for sports today."
	else:
		return "Please exercise with care today, watch out for the weather!"
number = int(input("Enter a number: "))
result = sport_recommender(number)
print(result)