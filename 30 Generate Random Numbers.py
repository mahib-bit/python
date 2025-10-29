import random

#print(help(random))
# low = 1
# high = 6
Whole_number = random.randint(1, 6) #For a random whole number 1 through 6
#Whole_number = random.randint(low , high)
print (Whole_number)

float_number = random.random() # For a random fractional number 0 through 1
print(float_number)

options = ("rock" , "paper", "scissors")

draw = random.choice(options)
print(draw)

deck_of_cards = ["2","3","4","5","6","7","8","9","10","K","Q","J","A"]
deck = random.shuffle(deck_of_cards)
print(deck)