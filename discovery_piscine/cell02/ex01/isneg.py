try:
	num = int(input())
except:
	print("Not a number")
else:
	if (num < 0) :
		print("This number is negative.")
	elif (num > 0) :
		print("This number is positive.")
	else :
		print("This number is both positive and negative.")
