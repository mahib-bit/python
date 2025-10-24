
foods = []
prices = []
total = 0

while True:
    food = input("Enter food item or type 'q' to quit: ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter price for {food}: $"))
        foods.append(food)
        prices.append(price)
        total += price

print("\n----Shopping Cart----")
for i in range(0,len(foods)):
    print(f"{foods[i]} ----${prices[i]:.2f}")
print(f"\nYour total is : ${total:.2f}")