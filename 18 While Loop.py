name = input("Enter your name: ")

while name == "":
    print("You must enter a name.")
    name = input("Enter your name: ")

print(f"Hello, {name}!")

age = int(input("Enter your age:"))

while age < 0:
    print("Age cannot be negative.")
    age = int(input("Enter your age:"))

print(f"You are {age} years old.")

#with while loop you don't need to use try and except block to handle invalid input