"""
CP1404/CP5632 Practical
Quick Picks
"""
import random
NUMBER_OF_OUTPUT = 6
MIN_OUTPUT = 1
MAX_OUTPUT = 45
NUMBER_OF_CHARS = 2

number_of_quick_picks = int(input("How many quick picks? "))


# def get_random_number(user_list):
#     number = random.randint(MIN_OUTPUT, MAX_OUTPUT)
#     if number in user_list:
#         get_random_number(user_list)
#     else:
#         user_list.append(f"{number:{NUMBER_OF_CHARS}}")


for i in range(number_of_quick_picks):
    collection = []
    for j in range(NUMBER_OF_OUTPUT):
        random_number = random.randint(MIN_OUTPUT, MAX_OUTPUT)
        while random_number in collection:
            random_number = random.randint(MIN_OUTPUT, MAX_OUTPUT)
        collection.append(random_number)
    collection.sort()
    for number in range(len(collection)):
        collection[number] = f"{collection[number]:{NUMBER_OF_CHARS}}"
    print(" ".join(collection))
