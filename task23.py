email = input("Enter your email: ")

if not email.startswith("@") and email.endswith(".com"):
    print(True)
else:
    print(False)