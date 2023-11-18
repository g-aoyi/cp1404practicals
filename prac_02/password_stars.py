"""Password Check with Functions"""


MIN_LENGTH = 8


def main():
    """Function docstring"""
    # statements...
    password = get_password("Password", "Your password is too short.")
    print_password(password)


def get_password(prompt, error):
    password = input(prompt)
    while len(password) < MIN_LENGTH:
        print(error)
        password = input(prompt)
    return password


def print_password(password):
    print("*" * len(password))


main()
