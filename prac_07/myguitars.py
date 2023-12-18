"""CP1404/CP5632 Practical"""

from prac_07.guitar import Guitar
MY_FILE = 'guitars.csv'
guitars = []

name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: ").strip())
    guitar = Guitar(name, year, cost)
    print(guitar)
    out_file = open(MY_FILE, 'a')
    print(f"{name},{year},{cost}", file=out_file)
    out_file.close()
    name = input("Name: ")

in_file = open(MY_FILE, 'r')
in_file.readline()
for line in in_file:
    parts = line.strip().split(',')
    guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
    guitars.append(guitar)
in_file.close()

guitars.sort()

for guitar in guitars:
    print(guitar)
