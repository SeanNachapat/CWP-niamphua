password = "Python is awesome"

correct = False

while (not correct):
	guess = input()
	if (guess == password):
		print("ACCESS GRANTED")
		correct = True
	else :
		print("ACCESS DENIED")
