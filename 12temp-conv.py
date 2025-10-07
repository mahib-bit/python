unit = input("What type of temparature is it? (C/F) :")
temp = input("Enter the temperature :")
try:
    temp = float(temp)
except ValueError:
    print("Invalid temperature value.")
    exit()

if unit == "C":
    temp = round((9*temp)/5+32,1)
    print(f"Temperature in Farenheit is : {temp}F")

elif unit == "F":
    temp = round((temp-32)*5/9,1)
    print(f"Temperature in Celcius is : {temp}C")

else :
    print(f"{unit} is a wrong measure of unit")