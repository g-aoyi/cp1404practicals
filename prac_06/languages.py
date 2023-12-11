"""CP1404/CP5632 Practical"""

from prac_06.programming_language import ProgrammingLanguage


python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

languages = [python, ruby, visual_basic]
dynamic_languages = []

for language in languages:
    if language.is_dynamic():
        dynamic_languages.append(language.name)

print("The dynamically typed languages are:")
for language in dynamic_languages:
    print(language)
