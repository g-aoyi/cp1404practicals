NAME_FILE = 'name.txt'
NUMBERS_FILE = 'numbers.txt'


def question_1():
    name = input("Name: ")
    out_file = open(NAME_FILE, 'w')
    print(name, file=out_file)
    out_file.close()


def question_2():
    in_file = open(NAME_FILE, 'r')
    print(in_file.read().strip())
    in_file.close()


def question_3():
    in_file = open(NUMBERS_FILE, 'r')
    numbers_list = in_file.readlines()
    result = int(numbers_list[0]) + int(numbers_list[1])
    print(result)


def question_4():
    total = 0
    in_file = open(NUMBERS_FILE, 'r')
    for line in in_file:
        total += int(line)
    print(total)


question_1()
question_2()
question_3()
question_4()
