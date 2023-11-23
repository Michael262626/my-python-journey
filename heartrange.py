age = int(input("Enter your age:"))

maximum_heartrate = 220 - age
print("maximum heartrate is:", maximum_heartrate)

target_heartrate_range = (85 * maximum_heartrate) / 100
print("Target heartrate is", target_heartrate_range)