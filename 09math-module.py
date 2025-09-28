import math

x = 9

print(math.pi)
print(math.e)

result = math.sqrt(x)
print(result)

y = 9.5
y = math.ceil(y)
print(y)

z = 9.9
z = math.floor(z)
print(z)

# Calculate the area of a circle
radius = float(input("Enter the radius of the area :"))
area = math.pi * pow(radius, 2)

print(f"The area of the circle is : {round(area,2)}")