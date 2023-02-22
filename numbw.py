number = int(input("Enter number: "))

if number > 1:
	steps = 0
	while number != 1:
		if number %2 != 0:
			numNew = 3 * number + 1
		else:
			numNew = number // 2
		print(number)
		number = numNew
		steps += 1
	print("steps =",steps)
else:
	print("Bad c0 value")
	
