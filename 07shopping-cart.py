item = input("What item you would like to buy? :")
qunatity = float(input("How many would you like to buy? :"))
price = float(input("How much does it cost? :"))

total= qunatity*price

print(f"You have bought {qunatity} {item}s")
print(f"The total price is : {round(total,2)}$")