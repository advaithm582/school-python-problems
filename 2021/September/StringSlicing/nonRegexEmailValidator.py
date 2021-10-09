email = input("EMAIL: ")
user, at, domain = email.partition("@")
check1 = domain == "gmail.com"
check2 = user.replace(".", "").replace("_", "").isalnum()

if check1 and check2:
    print("valid")
else:
    print("invalid")

#
