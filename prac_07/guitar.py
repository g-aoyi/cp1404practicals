"""CP1404/CP5632 Practical"""


class Guitar:

    def __init__(self, name, year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self):
        YEAR = 2023
        age = YEAR - self.year
        return age

    def is_vintage(self):
        age = self.get_age()
        return age >= 50
