email = input("Enter your varsity Email address :")
Index = email.index("2")

name = email[:Index]
ID = email[Index:email.index("@")]
domain = email[email.index("@")+1:]

print(f"Your name is : {name}")
print(f"Your ID is : {ID}")
print(f"Your domain is : {domain}")
