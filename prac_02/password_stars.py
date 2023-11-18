MIN_LENGTH = 8

password = input("Password: ")
while len(password) < MIN_LENGTH:
    print("Your password is too short.")
    password = input("Password: ")
print("*" * len(password))
