Beatles = []

Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("The appended list are:", Beatles)

# Some names to be added by the user
for members in range(4):
    Beatles.append(input("New band member: "))
print("The new list:\n", Beatles )

# Deleting last two elements
del Beatles[-1]
del Beatles[-1]
print("after deleding\n",Beatles )

# Inserting new member 
Beatles.insert(0, "RingoStarr")
print(Beatles)
print("The Final list:\n",len(Beatles))
