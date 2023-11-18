"""Password Check with Functions"""


MIN_LENGTH = 8


def main():
    """Function docstring"""
    # statements...
    password = get_password("Your password is too short")
    print_password(password)


def get_password(error):
    password = input("Password: ")
    while len(password) < MIN_LENGTH:
        print(error)
        password = input("Password: ")
    return password


def print_password(password):
    print("*" * len(password))


main()
