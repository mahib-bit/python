
for x in range(3):
    for y in range(1,6):
        print(y,end=" ")   # The default end is '\n'
    print() # To move to the next line after inner loop

rows = int(input("Enter number of rows:"))
columns = int(input("Enter number of columns:"))
symbol = input("Enter symbol to use:")

for x in range(rows):
    for y in range(columns):
        print(symbol,end ="")
    print()
    