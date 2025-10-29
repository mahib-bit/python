import random

low = 1
high = 100

guesses = 0
number = random.randint(low, high)

while True:
    guess =int(input(f"Enter a Number between  {low} - {high} :"))
    guesses +=  1

    if guess > number:
        print("Number is too high")
    elif guess < number:
        print("Number is too low")
    else:
        print("You have guessed correct!!")
        break

print(f"It took you {guesses} guesses this round")
