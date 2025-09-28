# Explicit type-casting (manually)
name = "Vyke"
age = 43
weight = 74.53
tarnished = True

print(type(name))  #Type() shows the type of the var

print(type(age))
age = float(age) # making integer a float
print(type(age))
print(age)

weight = int(weight) # making float integer
print(weight)

name = bool(name)
print(name)

age = bool(age) # boolean is only False when its 0
print(age)

# Implicit type-casting (automatically)
x = 5
y = 2.0

x = x/y

print(x)