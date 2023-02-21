private_number = 1574

print("Guess My private number to win a prize")

#promting the user to guess a number
user_number = int(input("Guess my private number: "))

#using while loop to see to see the correct guess
while user_number != private_number:
    print("You guessed it wrongly give another try")
    user_number = int(input("Enter the number again: "))

print(private_number, "Cograculations, you have won the Prize.")
