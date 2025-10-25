#dictionary = a collection of {key:value} pairs
#             ordered, changeable, and do not allow duplicates

Capitals = {"USA": "Washington DC",
            "France": "Paris",
            "Russia": "Moscow",
            "Bangladesh": "Dhaka"}

#print(dir(Capitals))
#print(help(Capitals.get))
print(Capitals.get("Russia"))  #Moscow
print(Capitals["France"])      #Paris
print(Capitals.get("Japan"))   #None

#To check if a key exists
if Capitals.get("Germany"):
    print("This Capital is present")
else:
    print("This Capital is not present")

Capitals.update({"Germany": "Berlin"})  #Adding new key:value pair
Capitals.update({"USA": "Detroit"})   #Updating existing key:value pair
Capitals.pop("Russia")             #Removing key:value pair
Capitals.popitem()              #Removes last inserted key:value pair
#Capitals.clear()              #Removes all key:value pairs
print(Capitals)

# To get all the  keys 
keys = Capitals.keys()
#print(keys)

for key in keys:
    print(key)
print()

# To get all the values
values = Capitals.values()
print(values)
for value in values:
    print(value)
print()

items = Capitals.items()
print(items)
print()
for item in items:
    print(item)
print()
for key , value in items:
    print(f"{key:^10} : {value:^10}")