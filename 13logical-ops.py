sunny = True

if not sunny :
    print("It's cloudy day")
else :
    print("It's sunny day")


temp = input("Enter the temperature :")
try:
    temp = float(temp)
except ValueError:
    print("Invalid temperature value.")
    exit()
if temp > 30 and temp < 50 :
    print("It's a hot day")

elif temp > 20 and temp <=30 :
    print("It's a nice day")
else:
    print("Temperature is out of expected range")