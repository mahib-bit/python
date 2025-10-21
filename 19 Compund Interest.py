
principal = 0
rate = 0
time = 0

while principal <=0:
    principal = float(input("Enter the principal amount: "))
    if principal <=0:
        print("Principal amount must be greater than zero.")

while rate <=0:
    rate = float(input("Enter the rate of intrest:"))
    if rate <=0 :
        print("Rate of intrest must be greater than zero.")

while time <=0:
    time = int(input("Enter the time period (in years):"))
    if time <=0 :
        print("Time period must be greater than zero.")

amount = principal * (1 + (rate/100)) **time
#amount = principal * (1 + pow((rate/100),time))

print(f"The total amount after {time} years is :${amount:.2f}")