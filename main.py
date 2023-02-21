year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
    if year % 4 != 0:
          print ("leap year")
        
    elif year % 400 != 0:
        print("common year")
    else:
        print("leap year")
        
