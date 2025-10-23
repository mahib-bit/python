fruits = [ "apple", "banana", "cherry", "date" ]

for x in range(0,len(fruits)):
    print(fruits[x])

#print(help(fruits)) # help() function shows all the methods available for the list object

print("apple" in fruits)  # Check if "apple" is in the list
print("grape" not in fruits)  # Check if "grape" is not in the list
print()
print(len(fruits))  # Get the length of the list
print()
fruits.append("elderberry")  # Add an item to the end of the list
print(fruits)
print()
fruits.remove("banana")  # Remove an item from the list
print(fruits) #  .pop() method removes the last item
print()

fruits[0] = "Mango"  # Changes the first item

for fruit in fruits:
    print(fruit)
print()
fruits.sort()  # Sort the list
fruits.reverse()  # Reverse the list
print(fruits)

print(fruits.index("cherry"))  # Get the index of an item
print(fruits.count("date"))  # Count occurrences of an item
fruits.clear()  # Clear the list
print(fruits)

fruits = {"apple", "banana", "cherry", "date"}
# {} is unordered and unindexed
print(fruits)