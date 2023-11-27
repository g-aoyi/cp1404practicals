"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When the value is of the wrong type
2. When will a ZeroDivisionError occur?
When attempting to divide by zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Check if the denominator is zero
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Invalid denominator")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")