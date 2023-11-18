for i in range(1, 21, 2):
    print(i, end=' ')
print()


def a():
    for i in range(0, 101, 10):
        print(i, end=' ')


def b():
    for i in range(20, 0, -1):
        print(i, end=' ')


def c():
    number = int(input("Number of stars: "))
    print("*" * number)


def d():
    number = int(input("Number of stars: "))
    for i in range(1, number + 1):
        print("*" * i, end='\n')


a()
print()
b()
print()
c()
print()
d()
