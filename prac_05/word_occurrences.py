"""
CP1404/CP5632 Practical
Word Occurrences
"""

word_to_value = {}
string_length = []

user_string = input("Text: ")
words = user_string.split()
for i in range(len(words)):
    if words[i] in word_to_value:
        word_to_value[words[i]] += 1
    else:
        word_to_value[words[i]] = 1

for key in word_to_value:
    string_length.append(len(key))

longest_string = max(string_length)
keys = sorted(word_to_value)

for i in range(len(keys)):
    print(f"{keys[i]:{longest_string}}: {word_to_value[keys[i]]}")
