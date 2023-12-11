"""
CP1404/CP5632 Practical
Emails
"""

email_to_name = {}


def main():
    user_email = input("Email: ").strip()
    while user_email != "":
        name = user_email.split("@")[0].title()
        if "." in name:
            name = " ".join(name.split(".")).title()
        reply = input(f"Is your name {name}? (Y/n) ").lower()
        if reply != "y" and reply != "":
            name = input("Name: ")
        email_to_name[name] = user_email
        user_email = input("Email: ").strip()
    for key in email_to_name:
        print(f"{key} ({email_to_name[key]})")


main()
