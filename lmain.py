hat_list = [1, 2, 3, 4, 5]  
x = int(input("Enter a number: "))
# to replace the middle number with an integer number entered by the user.
hat_list[2] = x
print(hat_list)
# line of code that removes the last element from the list.
del hat_list[-1]
# line of code that prints the length of the existing list.
print("the length of the list is: ", len(hat_list))
print(hat_list)