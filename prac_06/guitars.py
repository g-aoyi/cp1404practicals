"""CP1404/CP5632 Practical"""

from prac_06.guitar import Guitar

guitars = []
print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = int(input("Cost: "))
    guitar = Guitar(name, year, cost)
    print(guitar)
    guitars.append(guitar)
    name = input("Name: ")

for i, guitar in enumerate(guitars, 1):
    is_vintage = guitar.is_vintage()
    if is_vintage:
        vintage_string = " (vintage)"
    else:
        vintage_string = ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")