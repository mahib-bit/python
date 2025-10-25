menu = {"Pizza" : 8.50,
        "Hotdog" : 5.00,
        "Nachos" : 4.50,
        "Soda" : 2.00,
        "Chips" : 1.50,
        "Fries" : 3.00,
        "Burger" : 7.00,
        "Lemonade" : 4.35}

cart = [] #To store ordered items
total = 0
print("\n---------MENU---------")
for key ,value in menu.items():
    print(f"{key:^10} : ${value:>5.2f}")
print("----------------------")

while True:
    food = input("Select an item from the menu (or type 'q' to finish): ").capitalize()
    if food == "Q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
for food in cart:
    total += menu.get(food)
    print(food,end=" ")

print(f"\nYour Total is :${total:.2f}")