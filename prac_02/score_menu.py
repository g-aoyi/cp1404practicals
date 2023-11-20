MIN_SCORE = 0
MAX_SCORE = 100
MENU = "(G)et a valid score (must be 0-100 inclusive)\n(P)rint result (copy or import your function to determine the " \
       "result from score.py)\n(S)how stars (this should print as many stars as the score)\n(Q)uit"


def main():
    score = -1
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "g":
            score = get_valid_score("Score: ", "Invalid score")
        elif choice == "p":
            if score == -1:
                score = get_valid_score("Score: ", "Invalid score")
            result = get_result(score)
            print(result)
        elif choice == "s":
            if score == -1:
                score = get_valid_score("Score: ", "Invalid score")
            score = int(score)
            print("*" * score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").lower()


def get_valid_score(prompt, error):
    score = float(input(prompt))
    while score < 0 or score > 100:
        print(error)
        score = float(input(prompt))
    return score


def get_result(score):
    while score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
