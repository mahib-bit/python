# To print character at specific index in a string
# OR to print substring

credit_card = "1234-5678-9876-5432"
print(f"Character at index 0 is : {credit_card[0]}")
print(f"Character at index 5 is : {credit_card[5]}")
print(f"Substring from index 0 to 9 is : {credit_card[0:9]}")
# start index 0 is inclusive and 9 is exclusive
print(f"Substring from index 0 to 5 is : {credit_card[:5]}")
print(f"Substring from index 5 to 9 is : {credit_card[5:9]}")
# [ start : end : step ]
print(f"I only want to print  characters at even index : {credit_card[::2]}")
print(f"To reverse the whole string : {credit_card[::-1]}")
# Let's say we want to mask all characters except last 4 digits of credit card
last_four = credit_card[-4:]
print(f"Someone's Credit Card number : XXXX-XXXX-XXXX-{last_four}")