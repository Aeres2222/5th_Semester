name = input("Enter your name: ")
letters = len(name)
print("Number of letters is : " + str(letters))

if letters > 10:
    print("You have a big name")
else:
    print("You have a small name")