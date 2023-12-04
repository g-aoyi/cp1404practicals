"""
CP1404/CP5632 Practical
List Exercises
"""

NUMBER_OF_NUMBERS = 5

numbers = []
for i in range(NUMBER_OF_NUMBERS):
    user_number = int(input("Number: "))
    numbers.append(user_number)

first_number = numbers[0]
last_number = numbers[-1]
smallest_number = min(numbers)
largest_number = max(numbers)
average = sum(numbers) / len(numbers)
print(f"The first number is {first_number}\nThe last number is {last_number}\nThe smallest number if {smallest_number}\nThe largest number is {largest_number}\nThe average of the numbers is {average}")


USERNAMES = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Username: ")
if username in USERNAMES:
    print("Access granted")
else:
    print("Access denied")