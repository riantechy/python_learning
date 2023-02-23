hat_list = [1, 2, 3, 4, 5]  
x = int(input("Enter a number: "))

print("=================================================")
# to replace the middle number with an integer number entered by the user.
hat_list[2] = x
print(hat_list)
print("the length: ", len(hat_list))

print("=================================================")
# line of code that removes the last element from the list.
del hat_list[-1]
print(hat_list)
print("=================================================")
#adding another list using append
hat_list.append(7)
print(hat_list)
print("the length of the list after appending is: ", len(hat_list))

print("=================================================")
#inserting an element to a list
hat_list.insert(1, 20)
print(hat_list)
print("the length of the list after inserting new element is: ", len(hat_list))

print("=================================================")
#adding the elements in the list
sum = 0
for i in hat_list:
    sum += i
print("the sum of elements is", sum)

