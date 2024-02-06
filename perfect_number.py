def perfect_number():
	for index in range(1, 1000):
		sum =  0
		for count in range(1, index):
			if count % index == 0:
				sum+=count
			if sum == count:
				print(sum)
	
perfect_number()