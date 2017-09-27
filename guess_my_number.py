print("I'm going to guess your number between 1 and 100, if my guess is correct, type 'Correct'")
print("if my guess is too high type 'High' ")
print("If it's less than, press 'Low'")

lower_bound = 0
upper_bound = 100
number = int((upper_bound + lower_bound)/2)
done = False
tries = 0
guess = input(number)

while done != True:
	if guess == "High":
		upper_bound = number
		number = int((upper_bound + lower_bound)/2)
		guess = input(number)
	elif guess == "Low":
		lower_bound = number
		number = int((upper_bound + lower_bound)/2)
		guess = input(number)			
	elif guess == "Correct":
		print("I got it! And in only", tries, " tries")
		done = True
	tries += 1
print("See, the house always wins!!")

