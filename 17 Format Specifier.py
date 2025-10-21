price = 49.99
pi = 3.14159
negative = -42.56234

print(f"Pi is : {pi:.3f}")

print(f"Price is : {price:10}") #has 10 spaces default's right aligned
print(f"Price is : {price:<10}")#left aligned
print(f"Price is : {price:^10}")#center aligned
print(f"Price is : {price:>10}")#right aligned

print(f"price is : {price:0>10}") #fills with 0's
print(f"price is : {price:+}")  #shows the sign for positive numbers
print(f"Negative value is : {negative:+}") #doesnt change the sign

cost = 134554523.90235
print(f"Cost is : {cost:,}") #with comma as thousand separator
print(f"Cost is : {cost:+10,.2f}")