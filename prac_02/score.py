"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

MIN_SCORE = 0
MAX_SCORE = 100

# TODO: Fix this!


def main():
    score = float(input("Enter score: "))
    result = get_result(score)
    print(result)
    random_number = random.randint(MIN_SCORE, MAX_SCORE)
    print(random_number)


def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()


